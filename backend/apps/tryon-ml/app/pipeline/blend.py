import cv2
import os
import uuid

OUTPUT_DIR = "/tmp/tryon/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fake_tryon(avatar_path, garment_path, pose):
    avatar = cv2.imread(avatar_path)
    garment = cv2.imread(garment_path)

    if avatar is None or garment is None:
        raise ValueError("Failed to read avatar or garment image")

    garment_resized = cv2.resize(
        garment,
        (avatar.shape[1] // 2, avatar.shape[0] // 2),
    )

    x = avatar.shape[1] // 4
    y = avatar.shape[0] // 3

    avatar[y:y+garment_resized.shape[0], x:x+garment_resized.shape[1]] = garment_resized

    output_path = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}.jpg")
    cv2.imwrite(output_path, avatar)

    return output_path
