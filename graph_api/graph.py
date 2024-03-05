from collections import defaultdict
from typing import Any, Dict, List, Set, Tuple, Optional
from .exceptions import NodeNotFoundError


class Graph:
    """Undirected graph using adjacency list representation."""

    def __init__(self):
        self._adj: Dict[Any, Dict[Any, float]] = defaultdict(dict)

    def add_node(self, node: Any) -> None:
        if node not in self._adj:
            self._adj[node] = {}

    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        self._adj[u][v] = weight
        self._adj[v][u] = weight

    def neighbors(self, node: Any) -> Dict[Any, float]:
        if node not in self._adj:
            raise NodeNotFoundError(f"Node {node!r} not in graph")
        return dict(self._adj[node])

    @property
    def nodes(self) -> List[Any]:
        return list(self._adj.keys())

    @property
    def edges(self) -> List[Tuple[Any, Any, float]]:
        seen = set()
        edges = []
        for u in self._adj:
            for v, w in self._adj[u].items():
                if (v, u) not in seen:
                    edges.append((u, v, w))
                    seen.add((u, v))
        return edges

    def __len__(self) -> int:
        return len(self._adj)


class DiGraph(Graph):
    """Directed graph."""

    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        self.add_node(u)
        self.add_node(v)
        self._adj[u][v] = weight

    @property
    def edges(self) -> List[Tuple[Any, Any, float]]:
        edges = []
        for u in self._adj:
            for v, w in self._adj[u].items():
                edges.append((u, v, w))
        return edges
