uv init --app uv-fast-api && uv-fast-api

### FASTAPI
uv add "fastapi[standard]"

### RUFF
uv add --dev ruff

uv run ruff check .
uv run ruff check . --fix
uv run ruff format .

### Direct script
uv run python main.py

### DEV
uv run fastapi dev

### PROD
uv run fastapi run

## PostgreSQL setup

Set the database URL in .env:

DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/uv_fast_api

## Docs
http://localhost:8000/docs

## Feature 1 examples

### Create item

Request:

POST http://localhost:8000/feature-1/

Body:
{
	"name": "Sample item",
	"description": "Example payload"
}

Response (201):
{
	"id": 1,
	"name": "Sample item",
	"description": "Example payload",
	"created_at": "2026-02-08T12:34:56.789012+00:00"
}

## Simple PG DB examples

### Create item (ORM)

Request:

POST http://localhost:8000/simple-pg-db/orm

Body:
{
	"name": "Sample item"
}

Response (201):
{
	"id": 1,
	"name": "Sample item",
	"created_at": "2026-02-08T12:34:56.789012+00:00"
}