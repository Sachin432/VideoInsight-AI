from sentence_transformers import SentenceTransformer
from PIL import Image
import numpy as np

model = SentenceTransformer("clip-ViT-B-32")


def image_embedding(image_path):

    img = Image.open(image_path)

    embedding = model.encode(img)

    return np.array(embedding)


def text_embedding(text):

    embedding = model.encode(text)

    return np.array(embedding)
