from collections import deque


def recursive_dfs(graph, vertex):
    vertices = []

    vertices.append(vertex)

    def process(v):
        for adj in graph.edges[v]:
            if adj not in vertices:
                vertices.append(adj)
                process(adj)

    process(vertex)

    return vertices


def iterative_dfs(graph, vertex):
    vertices = []
    queue = deque()

    queue.append(vertex)

    while queue:
        v = queue.pop()
        if v not in vertices:
            vertices.append(v)
            for adj in reversed(graph.edges[v]):
                queue.append(adj)

    return vertices


def find_path(graph, vertex, target):
    vertices = []
    queue = deque([(vertex, None)])
    parents = {}

    while queue:
        v, parent = queue.pop()
        if v not in vertices:
            vertices.append(v)
            parents[v] = parent

            if v == target:
                break
            for adj in reversed(graph.edges[v]):
                queue.append((adj, v))

    path = [target]
    while parents[target]:
        target = parents[target]
        path.insert(0, target)

    return path
