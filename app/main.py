from fastapi import FastAPI, HTTPException, Query
from sqlmodel import Session, SQLModel, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from typing import Optional

from app.db import engine
from app.models import JobEvent
from app.schemas import JobEventCreate, PaginatedEvents

app = FastAPI(title="Job Tracker API")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/events", response_model=PaginatedEvents)
def list_events(limit: int = Query(default= 25, ge=1, le=100), offset: int = Query(default=0, ge=0), category: Optional[str] = Query(default=None), company: Optional[str] = Query(default=None), position: Optional[str] = Query(default=None)):
   with Session(engine) as session:

      base_stmt = select(JobEvent)

      if category:
         base_stmt = base_stmt.where(JobEvent.category == category)
      if company:
         base_stmt = base_stmt.where(JobEvent.company == company)
      if position:
         base_stmt = base_stmt.where(JobEvent.position == position)
   
      count_stmt = select(func.count()).select_from(base_stmt.subquery())
      total = session.exec(count_stmt).one()

      stmt = (base_stmt.order_by(JobEvent.received_at.desc()).offset(offset).limit(limit))

      items = session.exec(stmt).all()

      return PaginatedEvents(events=items, limit=limit, offset=offset, total=total, has_more=len(offset + limit)  < total,)
   
def get_events(session: Session, limit: int = 100):
   return session.exec(JobEvent).limit(limit).all()


@app.post("/events", status_code=201)
def create_event(payload: JobEventCreate):
   """
    Ingest a job lifecycle event.
    Idempotent on (source, external_id).
    """
   event = JobEvent(**payload.model_dump())
   with Session(engine) as session:
      session.add(event)
      try:
         session.commit()
         session.refresh(event)
      except IntegrityError:
         session.rollback()
         raise HTTPException(
            status_code=409,
            detail="Event already exists"
         )

   return event