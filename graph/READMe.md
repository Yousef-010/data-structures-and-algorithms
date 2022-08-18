# Code challenge 35: graph implementation 


> Graphs
- Graphs are non-linear data structure that consist of a set of nodes that are connected by edges.


>  Challenge
- Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods

- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph


>  Approach & Efficiency
- Big O Notation for all methods:

- add node:
  - Time Complexity: O(1)
  - Space Complexity: O(1)

- add edge:
  - Time Complexity: O(1)
  - Space Complexity: O(1)

- get nodes:
  - Time Complexity: O(1)
  - Space Complexity: O(1)

- get neighbors:
  - Time Complexity: O(1)
  - Space Complexity: O(1)

- size:
  - Time Complexity: O(1)
  - Space Complexity: O(1)


> Testing 
- Run `pytest .\tests\test_graph.py`
 

>  API

- _add_node()_: add a vertex to the graph.
- _add_edge()_: add an edge to connect two vertexes in a graph.
- _get nodes()_: return a collection of vertexes in the graph.
- _get neighbors()_: return all the connected vertexes for the given node.
- _size()_: return the number of the nodes in the graph