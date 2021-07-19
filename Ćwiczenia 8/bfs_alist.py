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

    return visited, d, parent


G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
start = 0
visited, d, parent = bfs(G, start)
print(visited, d, parent, sep="\n")