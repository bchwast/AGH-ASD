def dfs(G):
    n = len(G)
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G, v)
        time += 1

    visited = [False] * n
    parent = [None] * n
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    return visited, parent


G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
visited, parent = dfs(G)
print(visited, parent, sep="\n")