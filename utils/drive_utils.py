import gdown
import os
from app.constants import VIDEO_DIR
from app.logger import get_logger

logger = get_logger()

def download_from_drive(drive_url):

    file_id = drive_url.split("/d/")[1].split("/")[0]

    download_url = f"https://drive.google.com/uc?id={file_id}"

    output_path = os.path.join(VIDEO_DIR, f"{file_id}.mp4")

    gdown.download(download_url, output_path, quiet=False)

    logger.info("Downloaded video from Google Drive")

    return output_path