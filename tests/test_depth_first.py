import pytest
from graph.graph_depth_first.graph_depth_first import *


def test_exists_graph():
    """
    test the existance of a graph class
    """
    assert Graph


def test_empty_graph(empty_graph):
    """
    test the empty graph class
    """
    actual = empty_graph.size()
    expected = 0
    assert actual == expected


def test_depth_first_traversal_with_A_as_starting_point(graph):
    """
    test the depth first traversal within (A) as starting point method
    """
    actual = graph[0].depth_first(graph[1])
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'F', 'H']
    assert actual == expected


def test_depth_first_traversal_with_B_as_starting_point(graph):
    """
    test the depth first traversal within (B) as starting point method
    """
    actual = graph[0].depth_first(graph[2])
    expected = ['B', 'A', 'D', 'E', 'F', 'H', 'C', 'G']
    assert actual == expected


def test_depth_first_traversal_with_E_as_starting_point(graph):
    """
    test the depth first traversal within (E) as starting point method
    """
    actual = graph[0].depth_first(graph[3])
    expected = ['E', 'D', 'A', 'B', 'C', 'G', 'F', 'H']
    assert actual == expected


# ###########
# fixtures
# ###########

@pytest.fixture
def empty_graph():
    empty_graph = Graph()
    return empty_graph


@pytest.fixture
def graph():
    graph = Graph()
    A = graph.add_node('A')
    B = graph.add_node('B')
    C = graph.add_node('C')
    D = graph.add_node('D')
    E = graph.add_node('E')
    F = graph.add_node('F')
    G = graph.add_node('G')
    H = graph.add_node('H')

    graph.add_edge(A, B)
    graph.add_edge(A, D)
    graph.add_edge(B, C)
    graph.add_edge(C, G)
    graph.add_edge(D, E)
    graph.add_edge(D, F)
    graph.add_edge(D, H)

    graph.add_edge(B, D)
    graph.add_edge(F, H)
    return graph, A, B, E
