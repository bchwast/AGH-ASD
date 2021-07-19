def min_d(d, enqueued, n):
    best = float("inf")
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def dijkstra(G, s, t):
    def path(u):
        if parent[u] is None:
            return [u]
        return path(parent[u]) + [u]


    n = len(G)
    d = [(float("inf"))] * n
    parent = [None] * n
    enqueued = [True] * n

    d[s] = 0
    for i in range(n):
        u = min_d(d, enqueued, n)
        enqueued[u] = False

        for v in range(n):
            if 0 <= G[u][v] and d[u] + G[u][v] < d[v] and enqueued[v]:
                d[v] = G[u][v] + d[u]
                parent[v] = u

    route = path(t)
    return route


G = [[-1, 1, -1, -1, 5],
     [1, -1, 7, 8, 2],
     [-1, 7, -1, 1, -1],
     [-1, 8, 1, -1, 3],
     [5, 2, -1, 3, -1]]
print(dijkstra(G, 0, 2))