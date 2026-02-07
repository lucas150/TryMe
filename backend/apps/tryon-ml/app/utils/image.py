import requests
import os

INPUT_DIR = "/tmp/tryon/input"
os.makedirs(INPUT_DIR, exist_ok=True)


def download_image(url: str, filename: str):
    path = os.path.join(INPUT_DIR, filename)

    r = requests.get(url)
    r.raise_for_status()

    with open(path, "wb") as f:
        f.write(r.content)

    return path
