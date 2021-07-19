from queue import Queue

"""Mamy mapę miasteczka, w którym są domy i sklepy. Na mapie są również drogi (każda długości 1),
 które łączą dom z domem, albo dom ze sklepem. 
 Naszym zadaniem jest, dla każdego domu, znaleźć odległość do najbliższego sklepu."""

# używamy bfs'a, do kolejki wrzucamy wszystkie sklepy z odległością 0, uruchamiamy bfs'a z tą kolejką i zwiększamy
# licznik odległości o 1 przy wchodzeniu do nieodwiedzonego domu


def houses_and_shops(G):
    n = len(G)
    visited = [False] * n
    distance = [None] * n
    Q = Queue()
    for i in range(n):
        if G[i][0] == "S":
            Q.put(i)
            visited[i] = True
            distance[i] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u][1]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                Q.put(v)

    return distance

