from queue import Queue

# zapuszczamy bfs'a, kolorujemy wierzchołki grafu dwoma kolorami naprzemiennie falami


def bipartite_graph(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    colour = [None] * n
    Q = Queue()
    visited[s] = True
    colour[s] = "B"
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                if colour[u] == "B":
                    colour[v] = "R"
                else:
                    colour[v] = "B"
                parent[v] = u
                Q.put(v)
            else:
                if parent[v] != u:
                    if colour[v] == colour[u]:
                        return False

    return True


G = [[1, 3, 5], [0, 5], [4], [4, 0], [3, 2], [1, 0]]
start = 0
print(bipartite_graph(G, start))