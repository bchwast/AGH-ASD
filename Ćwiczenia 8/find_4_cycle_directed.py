# w każdym wierzchołku wykonuję dfs'a 3 razy, jeżeli w trzecim wykonaniu mogę wrócić do wierzchołka startowego to zna-
# lazłem cykl długości 4


def find_4_cycle(G):
    def dfs(u, cnt, start):
        visited[u] = True
        if cnt == 4:
            for v in G[u]:
                if v == start:
                    return [u]
            return []
        else:
            for v in G[u]:
                if not visited[v]:
                    parent[v] = u
                    return [u] + dfs(v, cnt + 1, start)
            return []

    n = len(G)
    visited = [False] * n
    parent = [None] * n
    for u in range(n):
        path = dfs(u, 1, u)
        if len(path) == 4:
            return path
        for i in range(n):
            visited[i] = False
            parent[i] = None

    return None


G = [[1], [2], [3], [0]]
print(find_4_cycle(G))