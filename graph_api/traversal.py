from collections import deque
from typing import Any, List, Set, Callable, Optional
from .graph import Graph


def bfs(graph: Graph, start: Any, visitor: Optional[Callable[[Any], None]] = None) -> List[Any]:
    visited: Set[Any] = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        if visitor:
            visitor(node)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs(graph: Graph, start: Any, visitor: Optional[Callable[[Any], None]] = None) -> List[Any]:
    visited: Set[Any] = set()
    order = []

    def _dfs(node: Any):
        visited.add(node)
        order.append(node)
        if visitor:
            visitor(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order
