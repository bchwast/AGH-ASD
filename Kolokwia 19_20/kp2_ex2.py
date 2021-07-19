# >= 1 pkt

from kp2_ex2_testy import runtests


def let( ch ): return ord(ch) - ord("a")


def min_d(d, enqueued, n):
    best = float("inf")
    vert = None
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def dijkstra(G, s, t):
    n = len(G)
    d = [(float("inf"))] * n
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

    return d[t]


def letters(G, W):
    n = len(G[0])
    w = len(W)
    big_G = [[-1] * ((n * w) + 2) for _ in range((n * w) + 2)]

    for e in G[1]:
        for i in range(w - 1):
            if G[0][e[0]] == W[i] and G[0][e[1]] == W[i + 1]:
                big_G[(i * n) + e[0]][((i + 1) * n) + e[1]] = e[2]
            elif G[0][e[0]] == W[i + 1] and G[0][e[1]] == W[i]:
                big_G[(i * n) + e[1]][((i + 1) * n) + e[0]] = e[2]

    for i in range(n):
        if G[0][i] == W[0]:
            big_G[n * w][i] = 0
        if G[0][i] == W[w - 1]:
            big_G[((w - 1) * n) + i][(n * w) + 1] = 0

    res = dijkstra(big_G, n * w, (n * w) + 1)
    return res
    

runtests( letters )
    
    
