from e2_ex3_testy import runtests


def topologic_sort(G):
    n = len(G)

    def dfs(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfs(G, v)
        res.append(u)

    visited = [False] * n
    res = []
    for u in range(n):
        if not visited[u]:
            dfs(G, u)

    res.reverse()
    return res


def tasks(T):
    n = len(T)
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if T[i][j] == 1:
                G[i].append(j)

    return topologic_sort(G)



runtests( tasks )
