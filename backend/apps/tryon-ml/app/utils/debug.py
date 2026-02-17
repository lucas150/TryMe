import os
import cv2

class DebugContext:
    def __init__(self, enabled: bool, base_path: str):
        self.enabled = enabled
        self.base_path = base_path

        # ✅ create request debug folder
        if self.enabled:
            os.makedirs(self.base_path, exist_ok=True)

    def log(self, msg: str):
        if self.enabled:
            print("[DEBUG]", msg)

    def save_image(self, name: str, img):
        if not self.enabled:
            return

        path = os.path.join(self.base_path, name)

        # Debug trace
        print("Saving debug image:", path)

        cv2.imwrite(path, img)
