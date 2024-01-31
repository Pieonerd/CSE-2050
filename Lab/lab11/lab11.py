class Graph_ES:
    def __init__(self, V=None, E=None):
        self.V = set()
        self.E = set()
        
        if V is not None:
            for v in V: self.add_vertex(v)

        if E is not None:
            for e in E: self.add_edge(e)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        if v not in self.V:
            raise KeyError(f"{v} not in Graph_ES, cannot remove")
        self.V.remove(v)

    def add_edge(self, e):
        self.E.add(e)
    
    def remove_edge(self, e):
        if e not in self.E:
            raise KeyError(f"{e} not in Graph_ES, cannot remove")
        self.E.remove(e)

    def _neighbors(self, v):
        nbrs = set()
        for e in self.E:
            if e[0] == v: nbrs.add(e[1])
        return nbrs

    def __len__(self):
        return len(self.V)

    def __iter__(self):
        return iter(self.V)

class Graph_AS:
    def __init__(self, V=None, E=None):
        self.V = set() # Set of vertices
        self.nbrs = dict() # Dictionary of neighbors
        # nbrs[vertex] = {connected_vertex}

        if V is not None:
            for v in V: self.add_vertex(v)

        if E is not None:
            for e in E: self.add_edge(e)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        if v not in self.V:
            raise KeyError(f"{v} not in Graph_AS, cannot remove")
        self.V.remove(v)

    def add_edge(self, e):
        a, b = e # a is e[0] and b is e[1]
        if a not in self.nbrs:
            self.nbrs[a] = {b}
        else: # a is already in the dictionary
            self.nbrs[a].add(b)
    
    def remove_edge(self, e):
        a, b = e
        if b not in self.nbrs[a]:
            raise KeyError(f"Vertex {a} has no neighbor {b}")
        self.nbrs[a].remove(b)
        if len(self.nbrs[a]) == 0: self.nbrs.pop(a)

    def _neighbors(self, v):
        if v not in self.nbrs:
            raise KeyError(f"Vertex{v} has no neighbors")
        return iter(self.nbrs[v])

    def __len__(self):
        return len(self.V)

    def __iter__(self):
        return iter(self.V)