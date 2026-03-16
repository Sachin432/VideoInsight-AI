import streamlit as st

from ingestion.video_storage import save_uploaded_video
from utils.drive_utils import download_from_drive

from processing.frame_extractor import extract_frames
from processing.embedding_generator import image_embedding

from retrieval.vector_store import add_embedding
from llm.langgraph_agent import run_agent

from utils.clip_generator import generate_clip

st.title("AI Video Query System")

video_path = None

uploaded_video = st.file_uploader("Upload video")

drive_link = st.text_input("Or paste Google Drive link")

if uploaded_video:

    video_path = save_uploaded_video(uploaded_video)

if drive_link:

    video_path = download_from_drive(drive_link)

if video_path:

    st.success("Video ready")

    if st.button("Index Video"):

        frames = extract_frames(video_path)

        for frame_path, ts in frames:

            emb = image_embedding(frame_path)

            add_embedding(
                emb,
                {
                    "frame": frame_path,
                    "timestamp": ts,
                    "video": video_path
                }
            )

        st.success("Video indexed")

query = st.text_input("Search video")

if st.button("Search"):

    results = run_agent(query)

    timestamps = []

    for r in results:

        ts = r["timestamp"]

        timestamps.append(ts)

        st.write(f"Timestamp: {ts}")

    if st.button("Generate Clips"):

        for ts in timestamps:

            clip = generate_clip(video_path, ts, ts + 5)

            st.video(clip)