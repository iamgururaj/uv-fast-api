**Prompt:**

Create a production-style feature module for a Python project using FastAPI and PostgreSQL.

Requirements:

* Directory: `app/features`
* Use latest stable ecosystem api (FastAPI, Pydantic, SQLAlchemy).
* Feature name: `simple_pg_db`.
* Include API layer, service layer, schemas, and database access.
* Use ORM for one version.
* Provide another version that uses plain SQL queries.
* Use Pydantic models for request/response validation.
* Keep business logic strictly inside the service.
* API must only handle HTTP concerns.
* Use dependency injection.
* Add realistic error handling.
* Use Python typing everywhere.
* Follow PEP8 (snake_case files).
* Keep code simple but production-real.
* Ready to run.

Structure expected:

```
app/features/<feature_name>/
    <feature_name>_api.py
    <feature_name>_service.py
    <feature_name>_schemas.py
    <feature_name>_models.py
    __init__.py
```

Also:

* database/session setup
* how router is registered in main app
* example create/get/list endpoints
* one example request
* one example response

Domain:

Use simple CRUD like create/get/list with a `name` field.

Return ORM objects in ORM version, dictionaries in raw SQL version.

Code should be clean, moderately detailed, and reflect real production practices.

---

If you want, I can also give stronger versions like:

* enterprise / DDD prompt
* async-first prompt
* microservice prompt
* clean architecture prompt
* test-driven prompt

Tell which level you want.
