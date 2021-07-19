# 1 pkt

from kp1_ex2_testy import runtests


def dfs(G, ign):
    n = len(G)

    def dfs_visit(G, u, ign):
        visited[u] = True

        for v in range(n):
            if v == ign:
                continue
            if G[u][v] != 0 and not visited[v]:
                parent[v] = u
                dfs_visit(G, v, ign)

    visited = [False] * n
    parent = [None] * n
    comps = 0
    for u in range(n):
        if u == ign:
            continue
        if not visited[u]:
            comps += 1
            dfs_visit(G, u, ign)

    return comps


def breaking(G):
    n = len(G)
    most = 1
    vert = None

    for u in range(n):
        curr = dfs(G, u)
        if curr > most:
            most = curr
            vert = u

    return vert


runtests( breaking )