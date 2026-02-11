# Pixel-level person segmentation using MediaPipe Selfie Segmentation. This provides a binary mask of the person in the image, which can be used for background removal and garment overlay.

# app/pipeline/parse.py

import numpy as np
from app.models.schp.inference import run_schp

# LIP label indices
UPPER_CLOTHES = 5   # ⚠️ double-check this
LEFT_ARM = 14
RIGHT_ARM = 15


def parse_human(image_path: str):
    parsing = run_schp(image_path)

    upper_clothes_mask = (parsing == UPPER_CLOTHES).astype(np.uint8)
    arms_mask = (
        (parsing == LEFT_ARM) |
        (parsing == RIGHT_ARM)
    ).astype(np.uint8)

    return {
        "parsing": parsing,
        "upper_clothes": upper_clothes_mask,
        "arms": arms_mask,
    }
