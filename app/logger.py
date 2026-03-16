from loguru import logger
import sys
import os
from app.constants import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "system.log")

logger.remove()

logger.add(
    LOG_FILE,
    rotation="20 MB",
    retention="10 days",
    level="INFO",
    enqueue=True
)

logger.add(sys.stdout, level="INFO")

def get_logger():
    return logger