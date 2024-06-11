from typing import Any, List, Set, Dict
from .graph import DiGraph
from .exceptions import CycleDetectedError


def topological_sort(graph: DiGraph) -> List[Any]:
    """Kahn's algorithm for topological sorting of DAG."""
    in_degree: Dict[Any, int] = {node: 0 for node in graph.nodes}
    for u, v, _ in graph.edges:
        in_degree[v] += 1

    queue = [node for node, deg in in_degree.items() if deg == 0]
    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)
        for v in graph.neighbors(u):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) != len(graph.nodes):
        raise CycleDetectedError("Graph contains at least one directed cycle")

    return result
