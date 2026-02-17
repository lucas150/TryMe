# Merge warped garment with avatar and human mask to create final try-on image
import cv2
import numpy as np
def blend_images(avatar_path, warped, mask):
    avatar = cv2.imread(avatar_path)

    mask = (mask > 0).astype(np.uint8)
    mask3 = np.stack([mask]*3, axis=2)

    result = avatar.copy()
    result[mask3 == 1] = warped[mask3 == 1]

    return result
