# TODO: SCHP / CIHP / LIP datasets for pose estimation


import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose


def estimate_pose(image_path: str):
    image = cv2.imread(image_path)
    if image is None:
        return None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(image_rgb)

    if not results.pose_landmarks:
        return None

    keypoints = []
    for idx, lm in enumerate(results.pose_landmarks.landmark):
        keypoints.append({
            "id": idx,
            "x": lm.x,
            "y": lm.y,
            "z": lm.z,
            "visibility": lm.visibility,
        })
    return keypoints


def draw_pose(image_path, pose):
    image = cv2.imread(image_path)
    h, w, _ = image.shape

    for kp in pose:
        x = int(kp["x"] * w)
        y = int(kp["y"] * h)
        cv2.circle(image, (x, y), 4, (0, 255, 0), -1)

    return image
