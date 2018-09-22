
from collections import deque

class Graph:

    '''minimal graph'''

    def  __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

class BFSResult:

    def  __init__(self):
        self.level = {}
        self.parent = {}

def bfs_simple(graph, start) :

    '''Queue-based minimal implementation of breath search first algorithm'''

    visited = [start]
    queue = [start]
    while queue:
        src = queue.pop(0)
        print(src)
        for dst in graph.adj[src]:
            if dst not in visited:
                visited.append(dst)
                queue.append(dst)
    return visited


def bfs_shortest(graph, src, dest):

    '''finds the shortest path of unweighted graph
    using breath search first algorithm'''

    path = [src]
    visited = [src]
    queue = [path] # queue is like [[o], [0,3], [0,4], [0,3,5], [0,3,7], [0,4,6]]
    while queue:
        current_path = queue.pop(0)
        last_node = current_path[-1]
        for v in graph.adj[last_node]:
            if v not in visited:
                visited.append(v)
                newpath = current_path.copy()
                newpath.append(v)
                if v == dest:
                    return newpath
                queue.append(newpath)
    print('not found')
    return

def bfs_tracked(graph, start) :

    '''Queue-based implementation of BFS.
    Args:
        graph: a graph with adjacency list adj such that
        graph.adj[u] is a list of u's neighbors.
        start: source.
    keeps track of all parents and levels
    '''

    r = BFSResult()
    r.parent = {start: None}
    r.level = {start: 0}
    queue = deque()
    queue.append(start)
    while queue:
        src = queue.popleft()
        for dst in graph.adj[src]:
            if dst not in r.level:
                r.parent[dst] = src
                r.level[dst] = r.level[src] + 1
                queue.append(dst)
    return r

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

    # bfs_simple(graph, 0)
    bfs_shortest(graph, 0, 6)

    print('finished')
