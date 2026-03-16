from ultralytics import YOLO
from app.logger import get_logger

logger = get_logger()

model = YOLO("yolov8n.pt")

def detect_objects(image_path):

    results = model(image_path)

    objects = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            objects.append(label)

    logger.info(f"Objects detected: {objects}")

    return objects