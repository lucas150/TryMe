# Merge warped garment with avatar and human mask to create final try-on image

import cv2
import numpy as np

# def blend_images(avatar_path, warped_image, human_mask):
#     avatar = cv2.imread(avatar_path)
#     mask = cv2.resize(human_mask, (avatar.shape[1], avatar.shape[0]))

#     alpha = mask.astype(float) * 0.7
#     alpha = alpha[:, :, None]

#     blended = (avatar * (1 - alpha) + warped_image * alpha).astype("uint8")
#     return blended

def blend_images(avatar_path, warped_image, human_mask):
    avatar = cv2.imread(avatar_path)
    mask = cv2.resize(human_mask, (avatar.shape[1], avatar.shape[0]))

    mask = mask.astype(np.float32)
    mask = cv2.GaussianBlur(mask, (21, 21), 0)

    alpha = mask[:, :, None]
    blended = avatar * (1 - alpha) + warped_image * alpha
    return blended.astype(np.uint8)
