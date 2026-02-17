import time
import uuid
import os
import cv2
import numpy as np  # <--- ADD THIS LINE

from app.config import DEBUG_MODE, DEBUG_DIR, OUTPUT_DIR
from app.utils.image import download_image
from app.pipeline.pose import estimate_pose, draw_pose
from app.pipeline.parse import parse_human
from app.pipeline.garment import preprocess_garment
from app.pipeline.warp import warp_garment
from app.pipeline.blend import blend_images
from app.utils.debug import DebugContext
from app.utils.pose_utils import pose_list_to_dict

def run_pipeline(avatar_url: str, garment_url: str, debug: bool = False):
    request_id = str(uuid.uuid4())
    debug_path = os.path.join(DEBUG_DIR, request_id)
    dbg = DebugContext(debug, debug_path)

    print("DEBUG ENABLED:", dbg.enabled)

    start = time.time()

    # --- 0. Download inputs ---
    avatar_path = download_image(avatar_url, "avatar")
    garment_path = download_image(garment_url, "garment")

    # Load avatar to get size
    avatar_img = cv2.imread(avatar_path)
    h, w = avatar_img.shape[:2]

    # --- 1. Pose estimation ---
    pose_raw = estimate_pose(avatar_path)
    if pose_raw is None:
        raise ValueError("Pose not detected")

    pose = pose_list_to_dict(pose_raw, w, h)

    print("POSE:", pose)

   

    pose_img = draw_pose(avatar_path, pose_raw)
    dbg.save_image("01_pose_overlay.jpg", pose_img)

    # --- 2. Human parsing ---
    human = parse_human(avatar_path, debug=dbg)
    parsing_raw = human["parsing"]

    dbg.log(f"Parsing classes: {np.unique(parsing_raw)}")

    upper_mask = human["upper_clothes"]
    arms_mask = human["arms"]

    garment_region = upper_mask * (1 - arms_mask)
    
    dbg.save_image("mask_upper.png", (upper_mask * 255).astype(np.uint8))
    dbg.save_image("mask_arms.png", (arms_mask * 255).astype(np.uint8))
    dbg.save_image("mask_final.png", (garment_region * 255).astype(np.uint8))


    # --- 3. Garment preprocessing ---
    garment_img, garment_mask = preprocess_garment(garment_path)

    if dbg.enabled:
        debug_viz = (parsing_raw * 12).astype(np.uint8)
        debug_viz_color = cv2.applyColorMap(debug_viz, cv2.COLORMAP_JET)
        dbg.save_image("02_parsing_debug.jpg", debug_viz_color)

    # --- 4. Warp garment ---
    warped = warp_garment(
        avatar_path,
        garment_img,
        garment_mask,
        pose,
        garment_region,
    )

    dbg.save_image("03_warped_garment.png", warped)

    # --- 5. Blend ---
    final_img = blend_images(
        avatar_path,
        warped,
        garment_region,
    )

    output_path = os.path.join(OUTPUT_DIR, f"{request_id}.jpg")
    cv2.imwrite(output_path, final_img)

    dbg.save_image("04_final_output.jpg", final_img)

    elapsed_ms = (time.time() - start) * 1000
    return output_path, elapsed_ms
