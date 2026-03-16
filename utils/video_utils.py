import cv2

def get_video_metadata(video_path):

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    duration = frame_count / fps

    cap.release()

    return {
        "fps": fps,
        "frames": frame_count,
        "duration": duration
    }