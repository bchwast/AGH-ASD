from e1_ex2_testy import runtests
from queue import PriorityQueue


def dijkstra(G, s, t):
    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight


    n = len(G)
    d = [float("inf")] * n
    enqueued = [True] * n
    Q = PriorityQueue()

    d[s] = 0
    cnt = 0
    Q.put((d[s], s))
    while not Q.empty() and cnt < n:
        u = Q.get()[1]
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]]:
                relax(u, v[0], v[1])
                Q.put((d[v[0]], v[0]))

    return d[t]


def robot( L, A, B ):
    w = len(L)
    k = len(L[0])
    n = w * k
    G = [[] for _ in range(12 * n)]

    for i in range(w):
        for j in range(k):
            if L[i][j] == "X":
                continue

            for s in [0, 1, 2, 6, 7, 8]:
                for t in [3, 9]:
                    G[(s * n) + (i * k) + j].append([(t * n) + (i * k) + j, 45])
            for s in [3, 4, 5, 9, 10, 11]:
                for t in [0, 6]:
                    G[(s * n) + (i * k) + j].append([(t * n) + (i * k) + j, 45])


            if j + 1 < k and L[i][j + 1] != "X":
                G[(0 * n) + (i * k) + j].append([(1 * n) + (i * k) + (j + 1), 60])
                G[(1 * n) + (i * k) + j].append([(2 * n) + (i * k) + (j + 1), 40])
                G[(2 * n) + (i * k) + j].append([(2 * n) + (i * k) + (j + 1), 30])

            if i + 1 < w and L[i + 1][j] != "X":
                G[(3 * n) + (i * k) + j].append([(4 * n) + ((i + 1) * k) + j, 60])
                G[(4 * n) + (i * k) + j].append([(5 * n) + ((i + 1) * k) + j, 40])
                G[(5 * n) + (i * k) + j].append([(5 * n) + ((i + 1) * k) + j, 30])

            if j - 1 >= 0 and L[i][j - 1] != "X":
                G[(6 * n) + (i * k) + j].append([(7 * n) + (i * k) + (j - 1), 60])
                G[(7 * n) + (i * k) + j].append([(8 * n) + (i * k) + (j - 1), 40])
                G[(8 * n) + (i * k) + j].append([(8 * n) + (i * k) + (j - 1), 30])

            if i - 1 >= 0 and L[i - 1][j] != "X":
                G[(9 * n) + (i * k) + j].append([(10 * n) + ((i - 1) * k) + j, 60])
                G[(10 * n) + (i * k) + j].append([(11 * n) + ((i - 1) * k) + j, 40])
                G[(11 * n) + (i * k) + j].append([(11 * n) + ((i - 1) * k) + j, 30])

    res = float("inf")
    for t in range(12):
        res = min(res, dijkstra(G, (A[1] * k) + A[0], (t * n) + (B[1] * k) + B[0]))

    if res == float("inf"):
        return None
    return res

    
runtests( robot )


