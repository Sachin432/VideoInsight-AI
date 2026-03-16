import os
import sys

# --- FIX PYTHON PATH ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import streamlit as st

from ingestion.video_storage import save_uploaded_video
from utils.drive_utils import download_from_drive

from processing.frame_extractor import extract_frames
from processing.embedding_generator import image_embedding

from retrieval.vector_store import add_embedding
from llm.langgraph_agent import run_agent

from utils.clip_generator import generate_clip


# ---------------- APP CONFIG ---------------- #

st.set_page_config(page_title="VideoInsight AI", layout="wide")

st.title("🎥 VideoInsight AI")
st.write("Search moments inside videos using AI")


# ---------------- SESSION STATE ---------------- #

if "video_path" not in st.session_state:
    st.session_state.video_path = None

if "timestamps" not in st.session_state:
    st.session_state.timestamps = []

if "indexed" not in st.session_state:
    st.session_state.indexed = False


# ---------------- VIDEO UPLOAD ---------------- #

st.header("Upload Video")

uploaded_video = st.file_uploader(
    "Upload video file",
    type=["mp4", "mov", "avi", "mkv"]
)

drive_link = st.text_input("Or paste Google Drive link")


if uploaded_video:

    st.session_state.video_path = save_uploaded_video(uploaded_video)
    st.session_state.indexed = False

    st.success("Video uploaded successfully")


if drive_link:

    st.session_state.video_path = download_from_drive(drive_link)
    st.session_state.indexed = False

    st.success("Video downloaded from Google Drive")


video_path = st.session_state.video_path


# ---------------- VIDEO INDEXING ---------------- #

if video_path:

    st.info(f"Video ready: {video_path}")

    if not st.session_state.indexed:

        if st.button("Index Video"):

            with st.spinner("Extracting frames and building embeddings..."):

                frames = extract_frames(video_path)

                progress = st.progress(0)

                for i, (frame_path, ts) in enumerate(frames):

                    emb = image_embedding(frame_path)

                    add_embedding(
                        emb,
                        {
                            "frame": frame_path,
                            "timestamp": ts,
                            "video": video_path
                        }
                    )

                    progress.progress((i + 1) / len(frames))

            st.session_state.indexed = True

            st.success("Video indexed successfully")

    else:

        st.success("Video already indexed")


# ---------------- SEARCH ---------------- #

st.header("Search Video")

query = st.text_input("Describe what you want to find")

if st.button("Search"):

    if not query.strip():

        st.warning("Please enter a search query")

    elif not video_path:

        st.warning("Please upload or download a video first")

    else:

        with st.spinner("Searching video..."):

            results = run_agent(query)

        timestamps = []

        if not results:

            st.warning("No results found")

        else:

            for r in results:

                ts = r.get("timestamp")

                if ts is not None:

                    timestamps.append(ts)

                    st.write(f"Match at timestamp: {round(ts,2)} seconds")

        st.session_state.timestamps = timestamps


# ---------------- CLIP GENERATION ---------------- #

if st.session_state.timestamps:

    st.header("Generate Clips")

    if st.button("Generate Clips"):

        for ts in st.session_state.timestamps:

            clip = generate_clip(video_path, ts, ts + 5)

            st.video(clip)
