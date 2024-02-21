from collections import deque


def bfs(graph, vertex):
    deque_ = deque([vertex])
    vertices = []

    while deque_:
        v = deque_.popleft()
        if v not in vertices:
            vertices.append(v)
            for adj in graph.edges[v]:
                deque_.append(adj)

    return vertices
