from graph_api import Graph, DiGraph, bfs, dfs, shortest_path


def test_undirected_graph_structure():
    g = Graph()
    g.add_edge("A", "B", weight=2.0)
    g.add_edge("B", "C", weight=3.0)

    assert len(g) == 3
    assert g.neighbors("B") == {"A": 2.0, "C": 3.0}


def test_bfs_traversal():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    order = bfs(g, start=1)
    assert order == [1, 2, 3, 4]


def test_shortest_path_dijkstra():
    g = Graph()
    g.add_edge("A", "B", weight=4)
    g.add_edge("A", "C", weight=2)
    g.add_edge("C", "B", weight=1)
    g.add_edge("B", "D", weight=5)

    path, cost = shortest_path(g, "A", "D")
    assert path == ["A", "C", "B", "D"]
    assert cost == 8.0
