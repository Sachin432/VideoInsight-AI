from typing import TypedDict, List, Dict, Any

from langgraph.graph import StateGraph, END

from llm.query_parser import parse_query
from retrieval.search_engine import search_video


# -------- State Schema -------- #

class AgentState(TypedDict):
    query: str
    parsed_query: str
    results: List[Dict[str, Any]]


# -------- Nodes -------- #

def query_node(state: AgentState) -> AgentState:
    query = state.get("query", "")
    parsed = parse_query(query)

    state["parsed_query"] = parsed
    return state


def search_node(state: AgentState) -> AgentState:
    parsed_query = state.get("parsed_query", "")

    results = search_video(parsed_query)

    state["results"] = results
    return state


# -------- Build Graph -------- #

builder = StateGraph(AgentState)

builder.add_node("query_parser", query_node)
builder.add_node("search", search_node)

builder.set_entry_point("query_parser")

builder.add_edge("query_parser", "search")
builder.add_edge("search", END)

graph = builder.compile()


# -------- Run Agent -------- #

def run_agent(query: str):

    result = graph.invoke({
        "query": query,
        "parsed_query": "",
        "results": []
    })

    return result.get("results", [])
