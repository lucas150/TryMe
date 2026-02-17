# Pixel-level person segmentation using MediaPipe Selfie Segmentation. This provides a binary mask of the person in the image, which can be used for background removal and garment overlay.

# app/pipeline/parse.py
import numpy as np

from app.models.schp.inference import run_segformer
from app.utils.debug import DebugContext

# LIP label indices
UPPER_CLOTHES = 5
LEFT_ARM = 14
RIGHT_ARM = 15


def parse_human(image_path: str, debug: DebugContext | None = None):
    parsing = run_segformer(image_path)

    if debug:
        debug.log("SegFormer parsing complete")

    upper_clothes_mask = (parsing == UPPER_CLOTHES).astype(np.uint8)

    arms_mask = (
        (parsing == LEFT_ARM) |
        (parsing == RIGHT_ARM)
    ).astype(np.uint8)

    if debug:
        debug.log("Masks extracted")

    return {
        "parsing": parsing,
        "upper_clothes": upper_clothes_mask,
        "arms": arms_mask,
    }
