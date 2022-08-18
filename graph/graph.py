class Graph:
    """
    A data structure representing a graph with a set of vertices and edges.
    """

    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        """
        Add node to graph
        :param: the value of the vertex
        :return: return the value of vertex
        """
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Adds an edge that connects two nodes of the graph
        :param start_vertex, end_vertex, weight
        :return: nothing
        """
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)
        edge2 = Edge(start_vertex)
        self.__adj_list[end_vertex].append(edge2)

    def get_nodes(self):
        """
        get all nodes within the graph
        :return: a collection  of nodes
        """
        return self.__adj_list.keys()

    def size(self):
        """
        Returns the size of the graph( as the number of nodes within it)
        :return: number
        """
        return len(self.__adj_list)

    def get_neighbors(self, vertex):
        """
        gets all the vertexes that connected to the given vertex in the graph
        :param vertex: vertex
        :return: a collection of edges connected to the given node
        """
        return self.__adj_list.get(vertex, [])


class Vertex:
    """
    Represents the nodes of a graph
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    """
    The Relations between the nodes for the graph
    """
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex



