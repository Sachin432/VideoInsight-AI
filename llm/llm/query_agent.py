from llm.query_parser import parse_query
from retrieval.search_engine import search_video


def run_agent(query: str):

    # Step 1: Parse query with LLM
    parsed_query = parse_query(query)

    # Step 2: Search vector database
    results = search_video(parsed_query)

    return results
