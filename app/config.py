import os
from dotenv import load_dotenv

# Try loading local .env for development
load_dotenv()

def get_secret(key, default=None):
    """
    Retrieve secret from Streamlit secrets or environment variables
    """

    try:
        import streamlit as st
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass

    return os.getenv(key, default)


class Config:

    # API KEYS
    GROQ_API_KEY = get_secret("GROQ_API_KEY")
    OPENAI_API_KEY = get_secret("OPENAI_API_KEY")
    HUGGINGFACE_TOKEN = get_secret("HUGGINGFACE_TOKEN")

    # Retrieval settings
    VECTOR_TOP_K = int(get_secret("VECTOR_TOP_K", 10))
    SIMILARITY_THRESHOLD = float(get_secret("SIMILARITY_THRESHOLD", 0.25))

    # Video processing
    FRAME_INTERVAL_SECONDS = int(get_secret("FRAME_INTERVAL_SECONDS", 1))
    MAX_VIDEO_SIZE_MB = int(get_secret("MAX_VIDEO_SIZE_MB", 500))


config = Config()