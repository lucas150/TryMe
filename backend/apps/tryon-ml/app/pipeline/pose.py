# app/pipeline/pose.py

import cv2
from mediapipe.python.solutions import pose as mp_pose


def estimate_pose(image_path: str):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not read image at {image_path}")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(image_rgb)

    return results.pose_landmarks
