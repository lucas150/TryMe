# Thin Plate Spline
# DensePose
# CP-VTON

import cv2

USE_CP_VTON = False  # switch later

def warp_garment(
    avatar_path,
    garment,
    garment_mask,
    pose,
    human_mask,
):
    avatar = cv2.imread(avatar_path)

    h, w, _ = avatar.shape
    garment = cv2.resize(garment, (w // 2, h // 2))

    x = w // 4
    y = h // 3

    warped = avatar.copy()
    warped[y:y+garment.shape[0], x:x+garment.shape[1]] = garment
    return warped
