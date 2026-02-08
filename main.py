from fastapi import FastAPI

from app.features.feature_1 import router as feature_1_router

app = FastAPI()

app.include_router(feature_1_router)


@app.get("/")
def read_root():
    return {"status": "success", "tool": "uv", "framework": "FastAPI"}
