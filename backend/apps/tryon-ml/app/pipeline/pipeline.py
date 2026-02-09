import time
import uuid
import os
import cv2

from app.config import DEBUG_MODE, DEBUG_DIR, OUTPUT_DIR
from app.utils.image import download_image
from app.pipeline.pose import estimate_pose, draw_pose
from app.pipeline.parse import parse_human
from app.pipeline.garment import preprocess_garment
from app.pipeline.warp import warp_garment
from app.pipeline.blend import blend_images


def run_pipeline(avatar_url: str, garment_url: str):
    request_id = str(uuid.uuid4())
    debug_path = os.path.join(DEBUG_DIR, request_id)
    os.makedirs(debug_path, exist_ok=True)

    start = time.time()
    # Download inputs
    avatar_path = download_image(avatar_url, "avatar")
    garment_path = download_image(garment_url, "garment")

    # 1. Pose
    pose = estimate_pose(avatar_path)
    if pose is None:
        raise ValueError("Pose not detected")

    if DEBUG_MODE:
        pose_img = draw_pose(avatar_path, pose)
        cv2.imwrite(f"{debug_path}/01_pose_overlay.jpg", pose_img)

    # 2. Human parsing
    human_mask = parse_human(avatar_path)

    if DEBUG_MODE:
        cv2.imwrite(f"{debug_path}/02_segmentation_mask.png", human_mask * 255)

    # 3. Garment preprocessing
    garment_img, garment_mask = preprocess_garment(garment_path)

    # 4. Warp garment
    warped = warp_garment(
        avatar_path,
        garment_img,
        garment_mask,
        pose,
        human_mask,
    )

    if DEBUG_MODE:
        cv2.imwrite(f"{debug_path}/03_warped_garment.png", warped)

    # 5. Blend
    final_img = blend_images(
        avatar_path,
        warped,
        human_mask,
    )

    output_path = os.path.join(OUTPUT_DIR, f"{request_id}.jpg")
    cv2.imwrite(output_path, final_img)

    if DEBUG_MODE:
        cv2.imwrite(f"{debug_path}/04_final_output.jpg", final_img)

    elapsed_ms = (time.time() - start) * 1000
    return output_path, elapsed_ms
