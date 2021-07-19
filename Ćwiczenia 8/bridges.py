def bridges(G):
    n = len(G)
    time = 0

    def dfs(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        d[u] = time
        low[u] = time

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs(G, v)
                low[u] = min(low[u], low[v])
            elif parent[u] != v:
                low[u] = min(low[u], low[v])


    visited = [False] * n
    d = [None] * n
    low = [None] * n
    parent = [None] * n

    for u in range(n):
        if not visited[u]:
            dfs(G, u)

    res = []
    for u in range(n):
        if d[u] == low[u] and parent[u] is not None:
            res.append((parent[u], u))

    return res


G = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
print(bridges(G))