from kp2_ex2_testy import runtests
# from queue import PriorityQueue


def let( ch ): return ord(ch) - ord("a")


# def find_word(G, W, s):
#     Q = PriorityQueue()
#     Q.put((0, s, 0))
#
#     m = float("inf")
#     while not Q.empty():
#         cost, u, ind = Q.get()
#         if ind == len(W) - 1:
#             m = min(m, cost)
#         else:
#             for v in range(len(G[u][1])):
#                 if G[u][1][v][2] == W[ind + 1]:
#                     Q.put((cost + G[u][1][v][1], G[u][1][v][0], ind + 1))
#     return m
#
#
# def letters( G, W ):
#     n = len(G[0])
#     graph = [[None, []] for _ in range(n)]
#     for i in range(n):
#         graph[i][0] = G[0][i]
#     for i in range(len(G[1])):
#         graph[G[1][i][0]][1].append((G[1][i][1], G[1][i][2], G[0][G[1][i][1]]))
#         graph[G[1][i][1]][1].append((G[1][i][0], G[1][i][2], G[0][G[1][i][0]]))
#
#     m = float("inf")
#     for i in range(n):
#         if graph[i][0] == W[0]:
#             m = min(m, find_word(graph, W, i))
#
#     if m == float("inf"):
#         return -1
#     return m


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
    
    
