import os
import ffmpeg
from app.constants import CLIP_DIR

def generate_clip(video_path, start, end):

    os.makedirs(CLIP_DIR, exist_ok=True)

    clip_name = f"clip_{int(start)}_{int(end)}.mp4"

    output_path = os.path.join(CLIP_DIR, clip_name)

    (
        ffmpeg
        .input(video_path, ss=start, to=end)
        .output(output_path)
        .run(overwrite_output=True)
    )

    return output_path