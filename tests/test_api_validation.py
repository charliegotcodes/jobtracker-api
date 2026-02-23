from app.main import app
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_post_events_invalid_payload_422():
    resp = client.post('/events', json={})
    assert resp.status_code == 422


def test_post_events_wrong_types_422():
    payload = {
        "event_type": 123,
        "source": True,
        "timestamp": "not_real_date",
    }
    resp = client.post('/events', json=payload)
    assert resp.status_code == 422

def test_post_events_rejects_non_json_422_415():
    resp = client.post('/events', data='not json', headers={"Content-Type": "text/plain"})
    assert resp.status_code in (422, 415)
    