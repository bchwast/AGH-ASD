from queue import PriorityQueue


def dijkstra(G, s, t):
    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight
            parent[v] = u

    def path(u):
        if parent[u] is None:
            return [u]
        return path(parent[u]) + [u]


    n = len(G)
    d = [float("inf")] * n
    parent = [None] * n
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

    route = path(t)
    return route


def two_drivers(G, x, y):
    n = len(G)
    big_G = [[] for _ in range(2 * n)]

    for i in range(n):
        for j in range(len(G[i])):
            big_G[i].append((n + G[i][j][0], G[i][j][1]))
            big_G[n + i].append((G[i][j][0], 0))
    big_G.append([(x, 0), (n + x, 0)])
    big_G.append([])
    big_G[y].append([(2 * n) + 1, 0])
    big_G[n + y].append([(2 * n) + 1, 0])
    route = dijkstra(big_G, (2 * n), (2 * n) + 1)

    path = [None] * (len(route) - 2)
    for i in range(len(route) - 2):
        path[i] = (route[i + 1]) % n

    if route[1] >= n:
        driver = "Bob"
    else:
        driver = "Alice"
    return driver, path


G = [[(1, 1), (4, 5)],
     [(0, 1), (2, 7), (3, 8), (4, 2)],
     [(1, 7), (3, 1)],
     [(2, 1), (1, 8), (4, 3)],
     [(0, 5), (1, 2), (3, 3)]]
print(two_drivers(G, 0, 3))
