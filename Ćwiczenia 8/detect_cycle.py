# wykorzystamy bfs'a, jeżeli trafimy na odwiedzony wierzchołek i nie jest on rodzicem obecnego wierzchołka, to graf,
# który badaliśmy posiada cykl


from queue import Queue


def detec_cycle_bfs(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    Q = Queue()
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.put(v)
            else:
                if parent[v] != u:
                    return True

    return False


G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
start = 0
print(detec_cycle_bfs(G, start))