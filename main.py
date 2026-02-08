from fastapi import FastAPI

from app.features.feature_1 import router as feature_1_router
from app.features.simple_pg_db import router as simple_pg_db_router


app = FastAPI()

app.include_router(feature_1_router)
app.include_router(simple_pg_db_router)


@app.get("/")
def read_root():
    return {"status": "success", "tool": "uv", "framework": "FastAPI"}
