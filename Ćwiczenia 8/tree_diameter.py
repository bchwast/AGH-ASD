from queue import Queue

"""Średnicą drzewa nazywamy odległość między jego najbardziej oddalonymi od siebie wierzchołkami.
 Napisz algorytm, który przyjmując na wejściu drzewo (niekoniecznie binarne!) w postaci listy krawędzi zwróci jego średnicę."""

# przechodzimy z listy krawędzi na listę sąsiedztwa, w dowolnym wierzchołku odpalamy bfs'a, następnie w wierzchołku,
# do którego dotarliśmy ponownie odpalamy bfs'a, ten bfs przejdzie przez średnicę tego drzewa, zatem w tablicy parent
# będziemy zapamiętywać drogę jaką przebył, żeby móc ją później odtworzyć


def bfs(G, u):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    Q = Queue()
    Q.put(u)
    visited[u] = True
    last = None

    while not Q.empty():
        u = Q.get()
        last = u
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.put(v)
    return last, parent

def path(parent, u):
    if parent[u] is None:
        return [u]
    return path(parent, parent[u]) + [u]

def tree_diameter(T):
    n = 0
    for i in range(len(T)):
        n = max(n, T[i][0], T[i][1])
    n += 1
    G = [[] for _ in range(n)]
    for i in range(len(T)):
        G[T[i][0]].append(T[i][1])
        G[T[i][1]].append(T[i][0])

    u, _ = bfs(G, 0)
    u, parent = bfs(G, u)
    diameter = path(parent, u)
    return diameter


T = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 6), (2, 7)]
print(tree_diameter(T))