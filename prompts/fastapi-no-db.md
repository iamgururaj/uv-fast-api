Create a production-style feature module for a Python project using FastAPI.

Requirements:
- Dir: app/features
- Feature name: feature_1
- No database.
- Include API layer, service layer, and schemas.
- Use Pydantic models for request and response validation.
- Keep business logic inside the service, not in the API.
- API should only handle HTTP concerns.
- Use dependency injection where appropriate.
- Add basic error handling.
- Use Python typing everywhere.
- Follow PEP8 naming (snake_case files).
- Keep it simple but realistic.

Structure expected:

features/<feature_name>/
    feature_1_api.py
    feature_1_service.py
    feature_1_schemas.py
    __init__.py

Also show:
- how the router is registered in the main app
- one example request
- one example response

Example domain:
Pick something simple like create/get/list.
Return in-memory data.

Code should be clear, moderately detailed, and ready to run.
