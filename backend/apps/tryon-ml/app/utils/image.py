import requests
import os
import uuid
from app.config import INPUT_DIR

def download_image(url: str, prefix: str):
    filename = f"{prefix}_{uuid.uuid4()}.jpg"
    path = os.path.join(INPUT_DIR, filename)

    r = requests.get(url, timeout=10)
    r.raise_for_status()

    with open(path, "wb") as f:
        f.write(r.content)

    return path
