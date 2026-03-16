import os

PROJECT_NAME = "Video Query AI"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = os.path.join(BASE_DIR, "data")

VIDEO_DIR = os.path.join(DATA_DIR, "videos")
FRAME_DIR = os.path.join(DATA_DIR, "frames")
CLIP_DIR = os.path.join(DATA_DIR, "clips")
INDEX_DIR = os.path.join(DATA_DIR, "index")

LOG_DIR = os.path.join(BASE_DIR, "logs")

SUPPORTED_VIDEO_FORMATS = [".mp4", ".avi", ".mov", ".mkv"]

FRAME_INTERVAL_SECONDS = 1

EMBEDDING_DIM = 512