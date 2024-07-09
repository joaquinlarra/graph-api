import json
from typing import Dict, Any
from .graph import Graph, DiGraph


def to_dict(graph: Graph) -> Dict[str, Any]:
    return {
        "directed": isinstance(graph, DiGraph),
        "nodes": graph.nodes,
        "edges": [{"from": u, "to": v, "weight": w} for u, v, w in graph.edges],
    }


def from_dict(data: Dict[str, Any]) -> Graph:
    g = DiGraph() if data.get("directed", False) else Graph()
    for node in data.get("nodes", []):
        g.add_node(node)
    for edge in data.get("edges", []):
        g.add_edge(edge["from"], edge["to"], weight=edge.get("weight", 1.0))
    return g
