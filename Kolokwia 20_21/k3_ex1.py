# 2 pkt

from k3_ex1_testy import runtests
from collections import deque


def path(parent, u, n):
    if parent[u] is None:
        return [(u // n, u % n)]
    return path(parent, parent[u], n) + [(u // n, u % n)]


def bfs(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    Q = deque()
    visited[s] = True
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.append(v)

    return parent


def floyd_warshall(G):
    n = len(G)
    S = [[G[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:
                S[i][j] = float("inf")

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]

    return S


def keep_distance(M, x, y, d):
    n = len(M)
    S = floyd_warshall(M)

    G = [[0] * (n * n) for _ in range(n * n)]
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if S[u][v] < d:
                continue
            for i in range(n):
                for j in range(n):
                    if i == v and j == u:
                        continue
                    if S[i][j] < d:
                        continue
                    if u == i and M[v][j] != 0:
                        G[(u * n) + v][(i * n) + j] = 1
                    elif v == j and M[u][i] != 0:
                        G[(u * n) + v][(i * n) + j] = 1
                    elif M[u][i] != 0 and M[v][j] != 0:
                        G[(u * n) + v][(i * n) + j] = 1

    parent = bfs(G, (x * n) + y)
    route = path(parent, (y * n) + x, n)

    return route


runtests( keep_distance )