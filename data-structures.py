"""
Robert Schwartz, 12/30/19

This file contains different implementations of data structures. This
file can be run through Terminal using the command [$ data-structures.py -v]
which also uses the provided doctests to check whether the code works.
"""

class Graph:
    
    def __init__(self, graph_dict = {}):
        """
        Parameters
        __________
        graph_dict : Dictionary

        The keys are the vertices of the graph, and the values are lists of
        adjacent vertices.
        """
        self.__graph_dict = graph_dict

    def vertices(self):
        """
        Returns a list of the vertices in the graph.
        """
        return list(self.__graph_dict.keys())

    def edges(self):
        """
        Returns a list of the edges in the graph.
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        Adds a key and value with an empty list if the vertex is not already in
        the graph.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        Must be of type set, tuple, or list; two vertices can have multiple
        edges.
        """
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.__graph_dict:
            self.__graph_dict[v1].append(v2)
        else:
            self.__graph_dict[v1] = v2

    def __generate_edges(self):
        """
        Static method for generating the graph's edges. Edges are represented
        as sets with one (loop) or two vertices.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "Vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nEdges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

if __name__ == "__main__":
    graph = { "a" : ["d"],
              "b" : ["c"],
              "c" : ["b", "c", "d", "e"],
              "d" : ["a", "c"],
              "e" : ["c"],
              "f" : [] }
    graph = Graph(graph)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("Add an edge:")
    graph.add_edge({"a","z"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
