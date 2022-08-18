import pytest
from graph.graph import *


def test_exists():
    assert graph


def test_empty_graph(empty_graph):
    actual = empty_graph.size()
    expected = 0
    assert actual == expected


def test_add_vertex_to_graph(empty_graph):
    empty_graph.add_node(5)
    actual = empty_graph.size()
    expected = 1
    assert actual == expected


def test_add_edge_to_graph(empty_graph):
    a = empty_graph.add_node('a')
    b = empty_graph.add_node('b')
    empty_graph.add_edge(a, b)
    actual = empty_graph.get_neighbors(a)[0].vertex
    expected = b
    assert actual == expected


def test_size_of_graph(graph):
    assert graph.size() == 5


def test_get_all_vertexes_in_graph(graph):
    result = []
    for i in graph.get_nodes():
        result.append(i.value)
    actual = result
    expected = ['A', 'B', 'E', 'C', 'D']
    assert actual == expected


def test_get_all_neighbors_of_vertex_in_graph(graph):
    nodes_array = []
    for i in graph.get_nodes():
        nodes_array.append(i)

    neighbors_array = []
    for i in graph.get_neighbors(nodes_array[0]):
        neighbors_array.append(i.vertex.value)

    result = []
    for i in neighbors_array:
        if i not in result:
            result.append(i)

    actual = result
    expected = ['B', 'E', 'C']
    assert actual == expected


def test_get_all_neighbors_of_vertex_in_graph_with_their_weights(graph):
    nodes_array = []
    for i in graph.get_nodes():
        nodes_array.append(i)

    neighbors_array = []
    for i in graph.get_neighbors(nodes_array[0]):
        neighbors_array.append([i.vertex.value, i.weight])

    result = []
    for i in neighbors_array:
        if i not in result:
            result.append(i)

    actual = result
    expected = [['B', 0], ['E', 0], ['C', 0]]
    assert actual == expected


def test_graph_with_only_one_node_and_edge(empty_graph):
    a = empty_graph.add_node("A")
    empty_graph.add_edge(a, a, 5)
    neighbors = empty_graph.get_neighbors(a)[0]

    assert empty_graph.size() == 1
    assert empty_graph.get_neighbors(a)[0].vertex.value == "A"
    assert neighbors.weight == 5


def test_raises_exception_start_vertex():
    graph = Graph()
    start = Vertex("start")
    end = graph.add_node("end")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_raises_exception_end_vertex():
    graph = Graph()
    end = Vertex("end")
    start = graph.add_node("start")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


@pytest.fixture
def graph():
    graph = Graph()

    a = graph.add_node('A')
    b = graph.add_node('B')
    e = graph.add_node('E')
    c = graph.add_node('C')
    d = graph.add_node('D')

    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(a, e)
    graph.add_edge(e, a)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(b, e)
    graph.add_edge(e, d)
    graph.add_edge(e, c)

    return graph


@pytest.fixture
def empty_graph():
    empty_graph = Graph()
    return empty_graph
