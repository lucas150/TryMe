def pose_list_to_dict(pose_list, image_w, image_h):
    pose_dict = {}

    for p in pose_list:
        pid = p["id"]

        px = int(p["x"] * image_w)
        py = int(p["y"] * image_h)

        if pid == 11:
            pose_dict["left_shoulder"] = (px, py)

        elif pid == 12:
            pose_dict["right_shoulder"] = (px, py)

    return pose_dict
