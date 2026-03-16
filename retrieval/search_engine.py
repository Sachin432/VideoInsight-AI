from processing.embedding_generator import text_embedding
from retrieval.vector_store import search_embedding

def search_video(query):

    query_vector = text_embedding(query)

    results = search_embedding(query_vector, k=10)

    return results