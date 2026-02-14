## Quick start

```bash
uv init --app uv-fast-api && uv-fast-api
uv add "fastapi[standard]"
uv add --dev ruff
```

## Common commands

| Task | Command |
| --- | --- |
| Run script | `uv run python main.py` |
| Dev server | `uv run fastapi dev` |
| Prod server | `uv run fastapi run` |
| Lint | `uv run ruff check .` |
| Lint (fix) | `uv run ruff check . --fix` |
| Format | `uv run ruff format .` |

## PostgreSQL setup

Set the database URL in `.env`:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/uv_fast_api
```

## API docs

http://localhost:8000/docs

## Feature 1 examples

### Create item

Request:

POST http://localhost:8000/feature-1/

Body:
```json
{
  "name": "Sample item",
  "description": "Example payload"
}
```

Response (201):
```json
{
  "id": 1,
  "name": "Sample item",
  "description": "Example payload",
  "created_at": "2026-02-08T12:34:56.789012+00:00"
}
```

## Simple PG DB examples

### Create item (ORM)

Request:

POST http://localhost:8000/simple-pg-db/orm

Body:
```json
{
  "name": "Sample item"
}
```

Response (201):
```json
{
  "id": 1,
  "name": "Sample item",
  "created_at": "2026-02-08T12:34:56.789012+00:00"
}
```