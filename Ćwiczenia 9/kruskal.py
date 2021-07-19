class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(G):
    G.sort(key=lambda x: x[2])
    n = 0
    for i in range(len(G)):
        n = max(n, G[i][0], G[i][1])
    n += 1

    v = [Node(i) for i in range(n)]
    A = []

    for e in G:
        if find(v[e[0]]) != find(v[e[1]]):
            A.append(e)
            union(v[e[0]], v[e[1]])

    return A


G = [(0, 1, 4), (0, 7, 8), (1, 0, 4), (1, 2, 8), (1, 7, 11), (2, 1, 8), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 2, 7),
     (3, 4, 9), (3, 5, 14), (4, 3, 9), (4, 5, 10), (5, 2, 4), (5, 3, 14), (5, 4, 10), (5, 6, 2), (6, 5, 2), (6, 7, 1),
     (6, 8, 6), (7, 0, 8), (7, 1, 11), (7, 8, 7), (7, 6, 1), (8, 7, 7), (8, 6, 6), (8, 2, 2)]
print(kruskal(G))

