from kp1_ex1_testy import runtests


def min_d(d, enqueued, n):
    best = float("inf")
    vert = None
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def path(parent, u, n):
    if parent[u] is None:
        return [u % n]
    return path(parent, parent[u], n) + [u % n]


def dijkstra(G, s, t, mult):
    n = len(G)
    d = [(float("inf"))] * n
    parent = [None] * n
    enqueued = [True] * n

    d[s] = 0
    for i in range(n):
        u = min_d(d, enqueued, n)
        if u is None:
            continue
        enqueued[u] = False

        for v in range(n):
            if 0 <= G[u][v] and d[u] + G[u][v] < d[v] and enqueued[v]:
                d[v] = G[u][v] + d[u]
                parent[v] = u

    res = t
    for i in range(mult):
        if d[(i * mult) + t] < d[res]:
            res = (i * mult) + t
    if d[res] == float("inf"):
        return parent, None
    return parent, res


def jak_dojade(G, P, d, a, b):
    n = len(G)
    big_G = [[-1] * ((d + 1) * n) for _ in range((d + 1) * n)]
    for u in range(n):
        for v in range(n):
            if G[u][v] > - 1 and G[u][v] <= d:
                if u in P:
                    for i in range(d + 1):
                        big_G[(i * n) + u][((d - G[u][v]) * n) + v] = G[u][v]
                else:
                    for i in range(d + 1):
                        if i - G[u][v] >= 0:
                            big_G[(i * n) + u][((i - G[u][v]) * n) + v] = G[u][v]

    parent, res = dijkstra(big_G, a, b, n)
    if res is None:
        return None
    route = path(parent, res, n)

    return route

        

runtests( jak_dojade ) 
