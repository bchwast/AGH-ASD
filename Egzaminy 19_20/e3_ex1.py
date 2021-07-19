# >= 1 pkt

from e3_ex1_testy import runtests
from queue import Queue


def bfs(G, s):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    parent = [None] * n
    Q = Queue()
    d[s] = 0
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)

    return max(d)


def best_root( L ):
    n = len(L)
    m = float("inf")
    res = -1
    for i in range(n):
        c_m = bfs(L, i)
        if c_m < m:
            res = i
            m = c_m

    return res


runtests( best_root ) 
