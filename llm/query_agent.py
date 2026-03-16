from llm.query_parser import parse_query
from retrieval.search_engine import search_video


def run_agent(query: str):

    parsed_query = parse_query(query)

    results = search_video(parsed_query)

    return results
