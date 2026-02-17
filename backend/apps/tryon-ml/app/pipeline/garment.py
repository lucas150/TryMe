# sleeve detection
# collar extraction
# category classification
import cv2
import numpy as np


def preprocess_garment(garment_path):
    garment = cv2.imread(garment_path)

    # convert to gray
    gray = cv2.cvtColor(garment, cv2.COLOR_BGR2GRAY)

    # remove white background
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # smooth edges
    mask = cv2.medianBlur(mask, 7)

    # binary mask
    mask = (mask > 0).astype(np.uint8)

    # remove noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    return garment, mask
