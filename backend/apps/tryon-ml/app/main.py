# ← FastAPI entrypoint

from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Try-On ML Service")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "ok", "service": "tryon-ml"}
