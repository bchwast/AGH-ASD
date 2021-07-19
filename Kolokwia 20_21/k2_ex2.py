from k2_ex2_testy import runtests
from collections import deque


def path(parent, u):
    if parent[u] is None:
        return [u]
    return path(parent, parent[u]) + [u]


def bfs(G, s, t, a, b):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    parent = [None] * n
    Q = deque()
    d[s] = 0
    visited[s] = True
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v] and not ((u == a and v == b) or (u == b and v == a)):
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)

    route = path(parent, t)
    return d[t], route


def enlarge(G, s, t):
    n = len(G)
    best, route = bfs(G, s, t, float("inf"), float("inf"))
    if best == -1:
        return None

    for i in range(1, len(route)):
        d, _ = bfs(G, s, t, route[i - 1], route[i])
        if d > best:
            return (route[i - 1], route[i])

    return None




runtests( enlarge ) 
