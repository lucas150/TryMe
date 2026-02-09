import cv2
import mediapipe as mp
import numpy as np

mp_selfie = mp.solutions.selfie_segmentation

def parse_human(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_selfie.SelfieSegmentation(model_selection=1) as segmenter:
        result = segmenter.process(image_rgb)

    mask = result.segmentation_mask
    binary = (mask > 0.5).astype(np.uint8)
    return binary
