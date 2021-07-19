from queue import Queue


def bfs(G, parent, s, t):
    n = len(G)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if not visited[v] and G[u][v] > 0:
                Q.put(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False


def edmonds_karp(G, s, t):
    n = len(G)
    parent = [None] * n
    max_flow = 0

    while bfs(G, parent, s, t):
        path_flow = float("inf")
        s_ = t
        while s_ != s:
            path_flow = min(path_flow, G[parent[s_]][s_])
            s_ = parent[s_]
        max_flow += path_flow

        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]
    return max_flow


G = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
print(edmonds_karp(G, 0, 5))
