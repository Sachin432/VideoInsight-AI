from langgraph.graph import StateGraph
from llm.query_parser import parse_query
from retrieval.search_engine import search_video


class State(dict):
    pass


def query_node(state):

    # Safe access to query
    query = state.get("query", "")

    parsed_query = parse_query(query)

    state["parsed_query"] = parsed_query

    return state


def search_node(state):

    parsed_query = state.get("parsed_query", "")

    results = search_video(parsed_query)

    state["results"] = results

    return state


builder = StateGraph(State)

builder.add_node("query_parser", query_node)
builder.add_node("search", search_node)

builder.set_entry_point("query_parser")

builder.add_edge("query_parser", "search")

graph = builder.compile()


def run_agent(query):

    result = graph.invoke({"query": query})

    return result.get("results", [])
