class AdjacencySetGraph:
    def __init__(self, V=(), E=()):
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for e in E: self.addedge(*e)

    def vertices(self):
        """Returns an iterator over the vertices in the graph"""
        return iter(self._V)
    
    def edges(self):
        """Returns an iterator over the edges in the graph"""
        for u in self._V:
            for v in self.nbrs(u):
                yield (u,v)

    def addvertex(self, v):
        """Adds a vertex to the graph"""
        self._V.add(v)
        self._nbrs[v] = set()

    def addedge(self, u, v):
        """Adds an edge to the graph"""
        self._nbrs[u].add(v)

    def removeedge(self, u, v):
        """Removes an edge from the graph"""
        self._nbrs[u].remove(v)

    def __contains__(self, v):
        """Determines if a vertex is in the graph"""
        return v in self._nbrs
    
    def nbrs(self, v):
        """Returns an iterator over the neighbors of a vertex"""
        return iter(self._nbrs[v])
    
    def __len__(self):
        """Returns the numer of vertices in the graph"""
        return len(self._nbrs)
    
class DiGraph(AdjacencySetGraph):
    def addedge(self, u, v, weight=1):
        """Adds a weighted edge to the graph"""
        self._nbrs[u][v] = weight

    def removeedge(self, u, v):
        """Removes a weighted edge from the graph"""
        del self._nbrs[u][v]

    def addvertex(self, v):
        """Adds a vertex to the graph"""
        self._V.add(v)
        self._nbrs[v] = {}

    def removevertex(self, v):
        """Removes a vertex and all its associated edges from the graph"""
        self._V.remove(v)
        del self._nbrs[v]
        for u in self._V:
            if v in self._nbrs[u]:
                del self._nbrs[u][v]

    def wt(self, u, v):
        """Returns the weight of a weighted edge"""
        return self._nbrs[u][v]