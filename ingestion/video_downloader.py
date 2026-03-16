import requests
import os
from app.constants import VIDEO_DIR
from app.logger import get_logger

logger = get_logger()

def download_video(url, filename):

    path = os.path.join(VIDEO_DIR, filename)

    r = requests.get(url, stream=True)

    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    logger.info(f"Video downloaded from {url}")

    return path