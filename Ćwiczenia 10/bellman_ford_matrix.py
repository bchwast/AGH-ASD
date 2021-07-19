def path(G, parent, u):
    if parent[u] is None:
        return [u]
    return path(G, parent, parent[u]) + [u]


def bellman_ford(G, s, t):
    n = len(G)
    d = [float("inf")] * n
    parent = [None] * n
    d[s] = 0

    for _ in range(n - 1):
        for i in range(n):
            for j in range(n):
                if d[i] != float("inf") and d[i] + G[i][j] < d[j]:
                    d[j] = d[i] + G[i][j]
                    parent[j] = i

    for i in range(n):
        for j in range(n):
            if d[i] != float("inf") and d[i] + G[i][j] < d[j]:
                return None

    route = path(G, parent, t)
    return route


G = [[float("inf"), 1, float("inf"), float("inf"), 5],
     [1, float("inf"), 7, 8, 2],
     [float("inf"), 7, float("inf"), 1, float("inf")],
     [float("inf"), 8, 1, float("inf"), 3],
     [5, 2, float("inf"), 3, float("inf")]]
print(bellman_ford(G, 0, 2))