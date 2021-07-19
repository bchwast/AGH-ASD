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
            for j in range(len(G[i])):
                if d[i] != float("inf") and d[i] + G[i][j][1] < d[G[i][j][0]]:
                    d[G[i][j][0]] = d[i] + G[i][j][1]
                    parent[G[i][j][0]] = i

    for i in range(n):
        for j in range(len(G[i])):
            if d[i] != float("inf") and d[i] + G[i][j][1] < d[G[i][j][0]]:
                return None

    route = path(G, parent, t)
    return route


G = [[(1, 1), (4, 5)],
     [(0, 1), (2, 7), (3, 8), (4, 2)],
     [(1, 7), (3, 1)],
     [(2, 1), (1, 8), (4, 3)],
     [(0, 5), (1, 2), (3, 3)]]
print(bellman_ford(G, 0 ,2))