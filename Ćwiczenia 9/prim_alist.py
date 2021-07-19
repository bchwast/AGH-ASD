from queue import PriorityQueue


def prim(G, s=0):
    n = len(G)
    key = [float("inf")] * n
    parent = [None] * n
    enqueued = [True] * n
    Q = PriorityQueue()

    key[s] = 0
    cnt = 0
    Q.put((key[s], s))
    while not Q.empty() and cnt < n:
        u = Q.get()[1]
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]] and v[1] < key[v[0]]:
                key[v[0]] = v[1]
                parent[v[0]] = u
                Q.put((key[v[0]], v[0]))
    return parent


# G = [[(1, 4), (7, 8)],
#      [(0, 4), (2, 8), (7, 11)],
#      [(1, 8), (3, 7), (5, 4), (8, 2)],
#      [(2, 7), (4, 9), (5, 14)],
#      [(3, 9), (5, 10)],
#      [(2, 4), (3, 14), (4, 10), (6, 2)],
#      [(5, 2), (7, 1), (8, 6)],
#      [(6, 1), (0, 8), (1, 11), (8, 7)],
#      [(2, 2), (6, 6), (7, 7)]]

G = [[(1, 1), (5, 12)],
     [(0, 1), (2, 5), (5, 7)],
     [(1, 5), (3, 3000), (4, 4), (5, 6)],
     [(2, 3000), (4, 9)],
     [(3, 9), (2, 4), (5, 8)],
     [(0, 12), (1, 7), (2, 6), (4, 8)]]
print(prim(G))



