# JobTracker API

A RESTful backend service for ingesting, storing, and managing job application lifecycle events.

## Overview
The JobTracker API is designed to persist job-related lifecycle events (e.g. applied, interview, rejection, offer) in an idempotent and structured way.

The project focuses on backend correctness, data integrity, and maintainable API-driven design, rather than UI concerns. It models real-world patterns commonly found in production systems that ingest external events.

## Key Features
- Idempotent event ingestion to prevent duplicate writes
- Relational data modeling using PostgreSQL
- Pagination and filtering for event retrieval
- Input validation and structured error handling
- Environment-based configuration for flexible local and future deployment

## Tech Stack
- Python
- FastAPI
- SQLModel
- PostgreSQL (primary datastore)

## High-Level Architecture
- **API layer** handles request validation and routing
- **Service layer** enforces idempotency and domain rules
- **Persistence layer** stores normalized lifecycle events in a relational schema

The service is designed to be stateless, allowing it to integrate cleanly with upstream ingestion services and support future deployment patterns.

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
