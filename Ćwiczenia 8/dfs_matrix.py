def dfs(G):
    n = len(G)
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        time += 1
        visited[u] = True

        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                parent[v] = u
                dfs_visit(G, v)
        time += 1

    visited = [False] * n
    parent = [None] * n
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    return visited, parent


G = [[0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]]
visited, parent = dfs(G)
print(visited, parent, sep="\n")