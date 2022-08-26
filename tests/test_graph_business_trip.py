import pytest
from graph.graph import *
from challengs.graph_business_trip.graph_business_trip import *


def test_Metroville_to_Pandora(graph):
    """
    test the cost from Metroville to Pandora
    """
    actual = business_trip(graph[0], [graph[1][2], graph[1][0]])
    expected = '$82'
    assert actual == expected


def test_Arendelle_to_Monstropolis_to_Naboo(graph):
    """
    test the cost from Arendelle to Naboo
    """

    actual = business_trip(graph[0], [graph[1][1], graph[1][3], graph[1][5]])
    expected = '$115'
    assert actual == expected


def test_Naboo_to_Pandora(graph):
    """
    test the cost from Naboo to Pandora
    """

    actual = business_trip(graph[0], [graph[1][5], graph[1][0]])
    expected = None
    assert actual == expected


def test_Narnia_to_Arendelle_to_Naboo(graph):
    """
    test the cost from Narnia to Naboo
    """

    actual = business_trip(graph[0], [graph[1][4], graph[1][1], graph[1][5]])
    expected = None
    assert actual == expected


# fixture ############ ############# ################ ################# ######

@pytest.fixture
def graph():
    all_cities_nodes = []
    graph = Graph()

    Pandora = graph.add_node('Pandora')
    all_cities_nodes.append(Pandora)
    Arendelle = graph.add_node('Arendelle')
    all_cities_nodes.append(Arendelle)
    Metroville = graph.add_node('Metroville')
    all_cities_nodes.append(Metroville)
    Monstropolis = graph.add_node('Monstropolis')
    all_cities_nodes.append(Monstropolis)
    Narnia = graph.add_node('Narnia')
    all_cities_nodes.append(Narnia)
    Naboo = graph.add_node('Naboo')
    all_cities_nodes.append(Naboo)

    graph.add_edge(Pandora, Arendelle, 150)
    graph.add_edge(Pandora, Metroville, 82)
    graph.add_edge(Arendelle, Pandora, 150)
    graph.add_edge(Arendelle, Metroville, 99)
    graph.add_edge(Arendelle, Monstropolis, 42)
    graph.add_edge(Metroville, Arendelle, 99)
    graph.add_edge(Metroville, Pandora, 82)
    graph.add_edge(Metroville, Monstropolis, 105)
    graph.add_edge(Metroville, Narnia, 37)
    graph.add_edge(Metroville, Naboo, 26)
    graph.add_edge(Monstropolis, Arendelle, 42)
    graph.add_edge(Monstropolis, Metroville, 105)
    graph.add_edge(Monstropolis, Naboo, 73)
    graph.add_edge(Naboo, Narnia, 250)
    graph.add_edge(Naboo, Metroville, 73)
    graph.add_edge(Naboo, Monstropolis, 26)
    graph.add_edge(Narnia, Naboo, 250)
    graph.add_edge(Narnia, Metroville, 37)

    return graph, all_cities_nodes
