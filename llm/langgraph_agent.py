from langgraph.graph import StateGraph
from llm.query_parser import parse_query
from retrieval.search_engine import search_video


# ----- Graph State -----

class State(dict):
    pass


# ----- Nodes -----

def query_node(state):

    query = state.get("query", "")

    parsed_query = parse_query(query)

    return {
        "query": query,
        "parsed_query": parsed_query
    }


def search_node(state):

    parsed_query = state.get("parsed_query", "")

    results = search_video(parsed_query)

    return {
        "results": results
    }


# ----- Build Graph -----

builder = StateGraph(State)

builder.add_node("query_parser", query_node)
builder.add_node("search", search_node)

builder.set_entry_point("query_parser")

builder.add_edge("query_parser", "search")

graph = builder.compile()


# ----- Run Agent -----

def run_agent(query):

    result = graph.invoke({
        "query": query
    })

    return result.get("results", [])
