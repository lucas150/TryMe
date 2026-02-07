        #    ← /tryon endpoint


from fastapi import APIRouter
from pydantic import BaseModel
from app.pipeline.pipeline import run_pipeline

router = APIRouter()   # 👈 THIS LINE IS CRITICAL

class TryOnRequest(BaseModel):
    avatar_image_url: str
    garment_image_url: str

class TryOnResponse(BaseModel):
    output_image_path: str
    time_ms: float

@router.post("/tryon", response_model=TryOnResponse)
def tryon(req: TryOnRequest):
    output_path, time_ms = run_pipeline(
        req.avatar_image_url,
        req.garment_image_url,
    )
    return {
        "output_image_path": output_path,
        "time_ms": time_ms,
    }
