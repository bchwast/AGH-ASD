"""Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyróżniony wierzchołek - korzeń.
 Każdy wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie."""

# przechodzimy po drzewie dfs'em, i zliczamy node'y, jak natrafimy na koniec poddrzewa to wracamy się wyżej i zwiększamy
# rozmiar o rozmiar zbadanego poddrzewa


def subtrees_size(T):
    def dfs_visit(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                size[u] += dfs_visit(G, v)

        return size[u]


    n = 0
    for i in range(len(T)):
        n = max(T[i][0], T[i][1], n)
    n += 1
    G = [[] for _ in range(n)]
    for i in range(len(T)):
        G[T[i][0]].append(T[i][1])
        G[T[i][1]].append(T[i][0])

    visited = [False] * n
    parent = [None] * n
    size = [1] * n
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    return size


T = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [1, 6], [3, 7], [3, 8], [5, 9], [5, 10], [8, 11], [9, 12], [10, 13],
     [10, 14], [10, 15], [11, 16], [16, 17], [17, 18], [17, 19]]
print(subtrees_size(T))