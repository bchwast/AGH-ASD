from queue import Queue


def bfs(G, parent, s, t):
    n = len(G)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if not visited[v] and G[u][v] > 0:
                Q.put(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False


def edmonds_karp(G, s, t):
    n = len(G)
    parent = [None] * n
    max_flow = 0

    while bfs(G, parent, s, t):
        path_flow = float("inf")
        s_ = t
        while s_ != s:
            path_flow = min(path_flow, G[parent[s_]][s_])
            s_ = parent[s_]
        max_flow += path_flow

        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]
    return max_flow


def edmonds_karp_mult(G, S, T):
    n_g = len(G)
    n = n_g + 2
    wanted_flow = 0

    big_G = [[0] * n for _ in range(n)]
    for i in range(n_g):
        for j in range(n_g):
            big_G[i][j] = G[i][j]

    # i = n_g   - superźródło
    for j in range(len(S)):
        big_G[n_g][S[j][0]] = S[j][1]
    # i = n_g + 1   - superujście
    for j in range(len(T)):
        big_G[T[j][0]][n_g + 1] = float("inf")
        wanted_flow += T[j][1]

    flow = edmonds_karp(big_G, n_g, n_g + 1)
    if flow == wanted_flow:
        return True
    return False


c = [[0 for j in range(5)] for i in range(5)]
c[0][2] = 2
c[0][3] = 3
c[1][2] = 2
c[1][4] = 3
s = [(0, 4), (1, 3)]
t = [(2, 3), (3, 1), (4, 3)]
print(edmonds_karp_mult(c, s, t))

