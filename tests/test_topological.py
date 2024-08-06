import pytest
from graph_api import DiGraph, topological_sort, CycleDetectedError, to_dict, from_dict


def test_topological_sort():
    g = DiGraph()
    g.add_edge("build", "test")
    g.add_edge("test", "deploy")

    order = topological_sort(g)
    assert order == ["build", "test", "deploy"]


def test_cycle_detection():
    g = DiGraph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")

    with pytest.raises(CycleDetectedError):
        topological_sort(g)


def test_json_roundtrip():
    g = DiGraph()
    g.add_edge(1, 2, weight=4.5)
    data = to_dict(g)
    g2 = from_dict(data)

    assert len(g2) == 2
    assert g2.neighbors(1) == {2: 4.5}
