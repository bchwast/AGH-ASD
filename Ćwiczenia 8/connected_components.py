# puszczamy dfs'a, za każdym razem, gdy wywołujemy dfs_visit nie rekurencyjnie to trafiamy do następnej spójnej skłądowej


def connected_components(G):
    n = len(G)

    def dfs_vist(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfs_vist(G, v)

    visited = [False] * n
    cnt = 0
    for u in range(n):
        if not visited[u]:
            cnt += 1
            dfs_vist(G, u)

    return cnt


G = [[1, 2], [0, 2], [0, 1], []]
print(connected_components(G))