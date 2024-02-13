class Graph:

    def __init__(self, edges=None):
        if edges is None:
            edges = {}
        self.edges = edges

    def add_edge(self, edge: tuple):

        v1, v2 = edge

        if v1 in self.edges:
            self.edges[v1].append(v2)

        else:
            self.edges[v1] = [v2]

        if v2 in self.edges:
            self.edges[v2].append(v1)
        else:
            self.edges[v2] = [v1]

    def get_vertices(self):
        return list(self.edges.keys())
