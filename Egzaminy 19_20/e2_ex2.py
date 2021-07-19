from e2_ex2_testy import runtests
from math import ceil, sqrt


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


def kruskal(V, E, beg):
    n = len(V)
    v = [Node(i) for i in range(n)]
    A = []

    for e in range(beg, len(E)):
        if find(v[E[e][0]]) != find(v[E[e][1]]):
            union(v[E[e][0]], v[E[e][1]])
            A.append(e)

    time = E[A[len(A) - 1]][2] - E[A[0]][2]
    for i in range(1, n):
        if find(v[0]) != find(v[i]):
            time = float("inf")
            break

    return time


def highway(A):
    n = len(A)
    V = [i for i in range(n)]
    E = []
    for i in range(n):
        for j in range(n):
            if i != j:
                E.append((i, j, ceil(sqrt((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2))))
    E.sort(key=lambda x: x[2])

    min_time = float("inf")
    for i in range(len(E)):
        min_time = min(min_time, kruskal(V, E, i))

    return min_time
        

runtests( highway ) 
