# app/pipeline/pipeline.py

import time
from app.pipeline.pose import estimate_pose
from app.pipeline.blend import fake_tryon
from app.utils.image import download_image


def run_pipeline(avatar_url: str, garment_url: str):
    start = time.time()

    avatar_path = download_image(avatar_url, "avatar.jpg")
    garment_path = download_image(garment_url, "garment.jpg")

    pose = estimate_pose(avatar_path)

    output_path = fake_tryon(
        avatar_path,
        garment_path,
        pose,
    )

    elapsed_ms = (time.time() - start) * 1000
    return output_path, elapsed_ms
