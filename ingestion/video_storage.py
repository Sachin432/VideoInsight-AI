import os
from app.constants import VIDEO_DIR
from app.logger import get_logger

logger = get_logger()

os.makedirs(VIDEO_DIR, exist_ok=True)

def save_uploaded_video(uploaded_file):

    video_path = os.path.join(VIDEO_DIR, uploaded_file.name)

    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    logger.info(f"Video saved at {video_path}")

    return video_path