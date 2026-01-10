from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID
from app.models import JobEvent

class JobEventCreate(BaseModel):
    source: str
    external_id: str
    category: str
    company: Optional[str] = None
    position: Optional[str] = None
    received_at: Optional[datetime] = None
    raw_subject: Optional[str] = None

class PaginatedEvents(BaseModel):
    events: list[JobEvent]
    limit: int
    offset: int
    total: int
    has_more: bool

class JobEventRead(BaseModel):
    id: UUID
    source: str
    category: str 
    company: Optional[str] = None
    position: Optional[str] = None
    received_at: datetime