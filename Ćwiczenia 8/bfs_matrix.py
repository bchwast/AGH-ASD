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
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                Q.put(v)

    return visited, d, parent


G = [[0, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]]
start = 0
visited, d, parent = bfs(G, start)
print(visited, d, parent, sep="\n")