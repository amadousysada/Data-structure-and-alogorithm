def dfs(graph, vertex):
    vertices = []

    vertices.append(vertex)

    def process(v):
        for adj in graph.edges[v]:
            if adj not in vertices:
                vertices.append(adj)
                process(adj)

    process(vertex)

    return vertices