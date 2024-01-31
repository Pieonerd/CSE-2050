from GraphHelper import DiGraph
from PriorityQueue import PriorityQueue

class Graph(DiGraph):
    def addedge(self, u, v, weight=1):
        """Add an undirected edge between vertices u and v with a given weight"""
        DiGraph.addedge(self, u, v, weight)
        DiGraph.addedge(self, v, u, weight)

    def removeedge(self,u, v):
        """Remove an undirected edge between vertices u and v"""
        DiGraph.removeedge(self, u, v)
        DiGraph.removeedge(self, v, u)

    def edges(self):
        """Return an iterator over the edges in the graph,
        where each edge is represented as a frozenset of its two vertices"""
        E = {frozenset(e) for e in DiGraph.edges(self)}
        return iter(E)
    
    def addvertex(self, v):
        """Add a vertex to the graph"""
        DiGraph.addvertex(self, v)

    def removevertex(self, v):
        """Remove a vertex and its incident edges from the graph"""
        DiGraph.removevertex(self, v)
    
    def fewest_flights(self, v):
        """Compute the fewest number of flights from a given vertex to all other vertices in the graph.
        Uses Dijkstra's algorithm with a priority queue"""
        tree = {v: None}
        D = {u: float('inf') for u in self.vertices()}
        D[v] = 0
        tovisit = PriorityQueue(entries = [(u, D[u]) for u in self.vertices()])
        for u in tovisit:
            for n in self.nbrs(u):
                if D[u] + 1 < D[n]:
                    D[n] = D[u] + 1
                    tree[n] = u
                    if n in tovisit._itemmap:
                        tovisit.changepriority(n, D[n])
        return tree, D

    def shortest_path(self, v):
        """Compute the shortest path from a given vertex to all other vertices in the graph.
        Uses Dijkstra's algorithm with a priority queue"""
        tree = {v: None}
        D = {u: float('inf') for u in self.vertices()}
        D[v] = 0
        tovisit = PriorityQueue(entries = [(u, D[u]) for u in self.vertices()])
        for u in tovisit:
            for n in self.nbrs(u):
                if D[u] + self.wt(u, n) < D[n]:
                    D[n] = D[u] + self.wt(u, n)
                    tree[n] = u
                    if n in tovisit._itemmap:
                        tovisit.changepriority(n, D[n])
        return tree, D

    def minimum_salt(self):
        """Compute the minimum spanning tree for the graph using Prim's algorithm with a priority queue"""
        v = next(iter(self.vertices()))
        tree = {}
        tovisit = PriorityQueue()
        tovisit.insert((None, v), 0)
        for a, b in tovisit:
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.insert((b, n ), self.wt(b, n))

        vertex_weights = {}
        for vertex in tree:
            for neighbor in self.nbrs(vertex):
                if neighbor == tree[vertex]:
                    vertex_weights[frozenset([vertex, neighbor])] = self.wt(vertex, neighbor)
                    
        return tree, vertex_weights