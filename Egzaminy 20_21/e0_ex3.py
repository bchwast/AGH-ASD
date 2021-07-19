from e0_ex3_testy import runtests


def min_d(d, enqueued, n):
    best = float("inf")
    vert = None
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def dijkstra(G, s, t, n):
    d = [(float("inf"))] * (2 * n)
    enqueued = [True] * (2 * n)

    d[s] = 0
    for i in range(2 * n):
        u = min_d(d, enqueued, 2 * n)
        if u is None:
            continue
        enqueued[u] = False

        for v in range(2 * n):
            if 0 <= G[u][v] and d[u] + G[u][v] < d[v] and enqueued[v]:
                d[v] = G[u][v] + d[u]

    res = min(d[t], d[n + t])
    return res


def jumper(G, s, w):
    n = len(G)
    big_G = [[-1] * (2 * n) for _ in range(2 * n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                big_G[i][j] = G[i][j]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                for k in range(n):
                    if G[j][k] != 0 and k != i:
                        if big_G[i][n + k] == -1:
                            big_G[i][n + k] = max(G[i][j], G[j][k])
                        else:
                            big_G[i][n + k] = min(big_G[i][n + k], max(G[i][j], G[j][k]))

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                big_G[n + i][j] = G[i][j]

    res = dijkstra(big_G, s, w, n)

    return res



runtests(jumper)