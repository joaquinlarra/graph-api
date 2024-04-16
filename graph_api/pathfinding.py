import heapq
from typing import Any, Dict, List, Optional, Tuple
from .graph import Graph
from .exceptions import NodeNotFoundError


def dijkstra(graph: Graph, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
    if source not in graph._adj:
        raise NodeNotFoundError(f"Source node {source!r} not in graph")

    distances: Dict[Any, float] = {node: float("inf") for node in graph.nodes}
    previous: Dict[Any, Optional[Any]] = {node: None for node in graph.nodes}
    distances[source] = 0.0

    pq: List[Tuple[float, Any]] = [(0.0, source)]

    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > distances[u]:
            continue

        for v, weight in graph.neighbors(u).items():
            alt = cur_dist + weight
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                heapq.heappush(pq, (alt, v))

    return distances, previous


def shortest_path(graph: Graph, source: Any, target: Any) -> Tuple[Optional[List[Any]], float]:
    distances, previous = dijkstra(graph, source)
    if distances.get(target, float("inf")) == float("inf"):
        return None, float("inf")

    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = previous[curr]
    path.reverse()
    return path, distances[target]
