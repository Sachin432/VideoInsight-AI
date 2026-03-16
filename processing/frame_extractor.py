import cv2
import os
from app.constants import FRAME_DIR
from app.logger import get_logger

logger = get_logger()

def extract_frames(video_path, interval=1):

    os.makedirs(FRAME_DIR, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_interval = int(fps * interval)

    frame_count = 0
    saved_frames = []

    video_name = os.path.basename(video_path).split(".")[0]

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:

            timestamp = frame_count / fps

            frame_name = f"{video_name}_{frame_count}.jpg"

            frame_path = os.path.join(FRAME_DIR, frame_name)

            cv2.imwrite(frame_path, frame)

            saved_frames.append((frame_path, timestamp))

        frame_count += 1

    cap.release()

    logger.info(f"{len(saved_frames)} frames extracted")

    return saved_frames