from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="Garment Try-On ML Service")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "ok", "service": "tryon-ml"}



# Given
# • a person image
# • a garment image

# → return a new image where the person is wearing the garment.