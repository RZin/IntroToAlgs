
class DiGraph:

    '''adjacency list based graph'''

    def  __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.adj = graph_dict

    def add_edge(self, src, dst):
        if src not in self.adj:
            self.adj[src] = []
        self.adj[src].append(dst)

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.adj.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.adj:
            for neighbour in self.adj[vertex]:
                if {vertex, neighbour} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for v in self.adj:
            res += str(v) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self.adj
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted
            double, i.e. every occurence of vertex in the list
            of adjacent vertices. """
        adj_vertices =  self.adj[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self.adj
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

class Graph(DiGraph):

    '''adjacency list based graph'''

    def  __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.adj = graph_dict

    def add_edge(self, src, dst):
        # forward
        if src not in self.adj:
            self.adj[src] = []
        self.adj[src].append(dst)
        # reverse
        if dst not in self.adj:
            self.adj[dst] = []
        self.adj[dst].append(src)

