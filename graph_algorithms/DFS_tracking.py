import pprint

class Node:
    def __init__(self, key):
        self.key = key

class Graph:

    def  __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

    def itervertices(self):
        for vertex in self.adj:
            yield vertex

    def neighbors(self, u):
        return self.adj[u]

class DFSResult:

    def __init__(self) :
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {}
        self.order = []
        self.t = 0

    def __str__(self):
        return """ self.parent = {}\n
        self.start_time = {}\n
        self.finish_time = {}\n
        self.edges = {}\n
        self.order = []\n
        self.t = 0\n """.format(self.parent,
        self.start_time,
        self.finish_time,
        self.edges,
        self.order,
        self.t)


def dfs(g):
    results = DFSResult()
    for vertex in g.itervertices():
        if vertex not in results.parent:
            dfs_visit(g, vertex, results)
    return results

def dfs_visit(g, v, results, parent = None):
    results.parent[v] = parent
    results.t += 1
    results.start_time[v] = results.t
    if parent:
        results.edges[(parent, v)] = 'tree'

    for n in g.neighbors(v):
        if n not in results.parent: # n is not visited.
            dfs_visit(g, n, results, v)
        elif n not in results.finish_time:
            results.edges[(v, n)] = 'back'
        elif results.start_time[v] < results.start_time[n]:
            results.edges[(v, n)] = 'forward'
        else:
            results.edges[(v, n)] = 'cross'

    results.t += 1
    results.finish_time[v] = results.t
    results.order.append(v)

def topological_sort(g):
    dfs_result = dfs(g)
    dfs_result.order.reverse()
    # print(dfs_result.edges)
    pprint.pprint(dfs_result.edges, compact=True)
    return dfs_result.order

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 3)
    graph.add_edge(0, 4)
    graph.add_edge(1, 3)
    graph.add_edge(2, 1)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(3, 5)
    graph.add_edge(3, 7)
    graph.add_edge(4, 6)
    graph.add_edge(4, 7)
    graph.add_edge(5, 1)
    graph.add_edge(6, 7)
    graph.add_edge(7, 5)

    # graph.add_edge(5, 8)
    # graph.add_edge(8, 9)
    # graph.add_edge(7, 9)

    # dfs(graph)
    # topological_sort(graph)
    print(dfs(graph))

    # N = int(input())
    # Tdata = [1, 1]
    # for count in range(2, N+1):
    #     Tdata.append(0)
    #     for root in range(1, count+1):
    #         Tdata[root] += Tdata[root-1] * Tdata[count - root]
    #
    # print(Tdata[N])

    print('finished')