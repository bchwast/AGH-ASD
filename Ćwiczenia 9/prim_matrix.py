def min_key(key, enqueued, n):
    best = float("inf")
    for u in range(n):
        if key[u] < best and enqueued[u]:
            best = key[u]
            vert = u
    return vert


def prim(G, s=0):
    n = len(G)
    key = [(float("inf"))] * n
    parent = [None] * n
    enqueued = [True] * n

    key[s] = 0
    for i in range(n):
        u = min_key(key, enqueued, n)
        enqueued[u] = False

        for v in range(n):
            if 0 < G[u][v] < key[v] and enqueued[v]:
                key[v] = G[u][v]
                parent[v] = u

    return parent


G = [[0, 1, 0, 0, 0, 12],
     [1, 0, 5, 0, 0, 7],
     [0, 5, 0, 3000, 4, 6],
     [0, 0, 3000, 0, 9, 0],
     [0, 0, 4, 9, 0, 8],
     [12, 7, 6, 0, 8, 0]]
print(prim(G))