
class Graph:

    '''minimal graph'''

    def  __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

def dfs_simple(graph, start, visited):

    '''basic graph traversing'''

    src = start
    print(src)
    if src in graph.adj:
        for dst in graph.adj[src]:
            if dst not in visited:
                visited.append(dst)
                visited = dfs_simple(graph, dst, visited)
    return visited

def dfs_topo(graph, start, visited, order):
    src = start
    # print(src)
    if src in graph.adj:
        for dst in graph.adj[src]:
            if dst not in visited:
                visited.append(dst)
                visited, order = dfs_topo(graph, dst, visited, order)
    order.append(src)
    return visited, order

def topological_sort(graph):
    visited = []
    order = []
    for src in graph.adj:
        if src not in visited:
            visited, order = dfs_topo(graph, src, visited, order)
    order = order[::-1]
    # print(order)
    return order

def topological_sort_from(graph, src):
    visited = [src]
    order = []
    visited, order = dfs_topo(graph, src, visited, order)
    order = order[::-1]
    # print(order)
    return order

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

    # dfs_simple(graph, 0, [])
    # topological_sort(graph)
    print(graph)
    topological_sort_from(graph, 0)
    print('finished')
