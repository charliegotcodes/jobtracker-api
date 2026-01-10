
JobEvent
- id (UUID)
- source
- external_id
- category (application, interview, rejected, offer)
- company (optional)
- position (optional)
- received_at
- raw_subject (optional)
- created_at


ENDPOINTS

POST /events
- ingest a job lifecycle event
- idempotent on (source, external_id)

GET /events
- paginated
- filterable by category, company, position
- ordered by received_at desc


ARCHITECTURE

- FastAPI + SQLModel
- Postgres (Supabase)
- Idempotent ingestion
- Deterministic parsing
- Pagination + filtering
- Designed for cron-based ingestion

FUTURE (v2)

- Application aggregation
- User accounts
- Auth
- Notes
- Status derivation


