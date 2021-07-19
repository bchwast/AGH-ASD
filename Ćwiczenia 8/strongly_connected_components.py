def strongly_connected_components(G):
    n = len(G)

    def dfs(G, u, stack):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfs(G, v, stack)

        stack.append(u)


    visited = [False] * n
    res = []
    for u in range(n):
        if not visited[u]:
            dfs(G, u, res)

    rev = [[] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            rev[j].append(i)

    visited = [False] * n
    components = []
    res.reverse()
    for u in res:
        if not visited[u]:
            comp = []
            dfs(rev, u, comp)
            components.append(comp)

    return components


G = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [9], [6, 7], [10], [8]]
print(strongly_connected_components(G))