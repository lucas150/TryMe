import cv2
import numpy as np
import cv2
import numpy as np

def warp_garment(
    avatar_path,
    garment_img,
    garment_mask,
    pose,
    garment_region,
):
    avatar = cv2.imread(avatar_path)
    h, w = avatar.shape[:2]

    canvas = np.zeros_like(avatar)

    # bounding box of garment region
    ys, xs = np.where(garment_region > 0)
    if len(xs) == 0 or len(ys) == 0:
        return canvas

    x1, x2 = xs.min(), xs.max()
    y1, y2 = ys.min(), ys.max()

    box_w = x2 - x1
    box_h = y2 - y1

    # resize garment
    garment_resized = cv2.resize(garment_img, (box_w, box_h))
    mask_resized = cv2.resize(
        garment_mask, (box_w, box_h),
        interpolation=cv2.INTER_NEAREST
    )

    mask_resized = mask_resized.astype(bool)

    roi = canvas[y1:y2, x1:x2]
    roi[mask_resized] = garment_resized[mask_resized]

    canvas[y1:y2, x1:x2] = roi

    return canvas
