# JobTracker API

A RESTful backend service for ingesting, storing, and managing job application lifecycle events.

## Overview
The JobTracker API persists job-related lifecycle events (e.g., Applied, Interview, Rejected, Offer) in a structured and idempotent manner.
This project focuses on backend correctness, data integrity, and maintainable API design. It models common production patterns found in systems that ingest external event data.

## Key Features
- Idempotent event ingestion using external event identifiers to prevent duplicate writes
- Relational data modeling using SQLModel with PostgreSQL (SQLite supported for local development)
- Filtering and pagination for querying lifecycle events
- Request validation using Pydantic schemas
- Structured error handling and logging

Environment-based configuration for flexible local and deployment setups
## Tech Stack
- Python
- FastAPI
- SQLModel
- PostgreSQL (primary datastore)

## High-Level Architecture
- **API layer** handles request validation and routing
- **Service layer** enforces idempotency and lifecycle rules
- **Persistence layer** stores normalized lifecycle events in a relational schema

The service is designed to be stateless, allowing it to integrate cleanly with upstream ingestion services via RESTful endpoints.

## Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL (or SQLite for local development)

### Setup
1. Clone the repository
2. Copy `.env.example` to `.env` and adjust values for your local environment
3. Install dependencies:
   ```bash

   pip install -r requirements.txt

