from queue import Queue

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

"""Prosze zaimplementowac algorytm BFS tak, zeby znajdował
 najkrótsze sciezki w grafie i nastepnie, zeby dało sie wypisac najkrotsza sciezke z zadanego punktu startowego
 do wskazanego wierzchołka."""

# odpalamy bfs'a, zapisujemy wierzchołki, z których weszliśmy do danych, sam bfs znajdzie nam najkrótszą ścieżkę
# rekurencyjną funkcją cofając się po parentach dostaniemy rozwiązanie


def path(parent, u):
    if parent[u] is None:
        return [u]
    return path(parent, parent[u]) + [u]

def bfs(G, s, f):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    Q = Queue()
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        while G[u] is not None:
            if not visited[G[u].val]:
                visited[G[u].val] = True
                parent[G[u].val] = u
                Q.put(G[u].val)
                G[u] = G[u].next

    if parent[f] is not None:
        return path(parent, f)
    return None


# a = Node(0)
# b = Node(1)
# c = Node(2)
# d = Node(3)
# e = Node(4)
# a.next = b
# b.next = c
# G = [a]
G = [[1, 2], [0], [0, 3], [2, 4], [3]]
print(bfs(G, 0, 4))