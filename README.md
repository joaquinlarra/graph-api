# graph-api

[![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)]()

Zero-dependency graph data structures, pathfinding algorithms, and topological sorting in modern Python.

## Features

- **Adjacency Lists**: Directed (`DiGraph`) and undirected (`Graph`) weighted representations.
- **Pathfinding**: Optimized Dijkstra shortest path solver and path reconstruction.
- **Traversals**: Non-recursive BFS and recursive DFS visitors.
- **DAG Operations**: Kahn's topological sort with automatic cycle detection (`CycleDetectedError`).
- **Data Serialization**: JSON-friendly export and import utilities.

---

## Installation

```bash
pip install graph-api-toolkit
```

---

## Quick Example

```python
from graph_api import Graph, DiGraph, shortest_path, topological_sort

# 1. Shortest Path with Dijkstra
g = Graph()
g.add_edge("A", "B", weight=3)
g.add_edge("A", "C", weight=1)
g.add_edge("C", "B", weight=1)
g.add_edge("B", "D", weight=4)

path, cost = shortest_path(g, "A", "D")
print(f"Shortest path: {path} (total cost: {cost})")
# Output: Shortest path: ['A', 'C', 'B', 'D'] (total cost: 6.0)

# 2. Dependency Resolution with Topological Sort
dag = DiGraph()
dag.add_edge("prep", "compile")
dag.add_edge("compile", "link")
dag.add_edge("link", "test")

print("Execution order:", topological_sort(dag))
```

---

## Running Tests

```bash
pip install -r requirements-dev.txt
pytest -v
```

---

## License
MIT © [Joaquin Astelarra](https://github.com/joaquinlarra)
