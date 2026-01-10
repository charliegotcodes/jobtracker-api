from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional

from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint

class JobEvent(SQLModel, table=True):
    __tablename__ ="job_events"
    __table_args__ = (UniqueConstraint("source", "external_id", name="unique_source_external_id"),)

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    source: str
    external_id: str
    category: str
    company: Optional[str] = None
    position: Optional[str] = None
    received_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    raw_subject: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))