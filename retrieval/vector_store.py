import faiss
import numpy as np
import os
import pickle
from app.constants import INDEX_DIR
from app.constants import EMBEDDING_DIM

os.makedirs(INDEX_DIR, exist_ok=True)

index = faiss.IndexFlatL2(EMBEDDING_DIM)

metadata = []

def add_embedding(vector, meta):

    vector = np.array([vector]).astype("float32")

    index.add(vector)

    metadata.append(meta)


def search_embedding(vector, k=5):

    vector = np.array([vector]).astype("float32")

    D, I = index.search(vector, k)

    results = []

    for idx in I[0]:

        results.append(metadata[idx])

    return results


def save_index():

    faiss.write_index(index, os.path.join(INDEX_DIR, "video.index"))

    with open(os.path.join(INDEX_DIR, "metadata.pkl"), "wb") as f:
        pickle.dump(metadata, f)


def load_index():

    global index
    global metadata

    index = faiss.read_index(os.path.join(INDEX_DIR, "video.index"))

    with open(os.path.join(INDEX_DIR, "metadata.pkl"), "rb") as f:
        metadata = pickle.load(f)