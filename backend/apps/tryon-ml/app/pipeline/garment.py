# sleeve detection
# collar extraction
# category classification

import cv2
import numpy as np

def preprocess_garment(garment_path):
    garment = cv2.imread(garment_path)

    gray = cv2.cvtColor(garment, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    mask = mask // 255
    return garment, mask
