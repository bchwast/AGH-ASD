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


G = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]
print(topologic_sort(G))