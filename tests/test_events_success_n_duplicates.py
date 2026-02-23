from fastapi.testclient import TestClient
from app.main import app 
import uuid

from sqlmodel import Session, select
from app.db import engine
from app.models import JobEvent

client = TestClient(app)

VALID_EVENT = {
    'event_type': "applied",
    'source': "gmail",
    "occurred_at": "2026-02-23T12:00:00Z",
    'external_id': "msg_123",
}

def make_valid_event():
    return {
    "source": "gmail",
    "external_id": f"msg_{uuid.uuid4()}",
    "category": "application_received",
    "company": "Acme Corp",
    "position": "Backend Developer",
    "received_at": "2026-02-12T00:23:35.840Z",
    "raw_subject": "Application received — Backend Developer at Acme Corp"
    }

def test_post_events_success_return_200_201():
    payload = make_valid_event()
    resp = client.post('/events', json=payload)
    assert resp.status_code in (200, 201), resp.text

def test_post_events_duplicate_idempotent():
    payload = make_valid_event()

    r1 = client.post('/events', json=payload)
    assert r1.status_code in (200, 201), r1.text

    r2 = client.post('/events', json=payload)
    assert r2.status_code in (200, 201, 409), r2.text

    with Session(engine) as session:
        events = session.exec(
            select(JobEvent).where(
                JobEvent.source == payload["source"],
                JobEvent.external_id == payload['external_id'],
            )
        ).all()

    assert len(events) == 1

