from queue import Queue, PriorityQueue

"""Dany jest graf ważony  G, oraz drzewo rozpinające T zawierające wierzchołek s. Podaj algorytm, który sprawdzi,
 czy T jest drzewem najkrótszych ścieżek od wierzchołka s."""

# przechodzimy G idąc po krawędziach z T i przypisujemy wierzchołkom odległości od s
# uruchamiamy algorytm Dijkstry, jeżeli w którymkolwiek momencie nastąpi relaksacja wierzchołka to podane drzewo T
# nie jest drzewem najkrótszych ścieżek od wierzchołka s


def bfs(G, s):
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    Q = Queue()

    d[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in range(len(G[u])):
            if not visited[G[u][v][0]]:
                visited[G[u][v][0]] = True
                d[G[u][v][0]] = d[u] + G[u][v][1]
                Q.put(G[u][v][0])
    return d


def spt(G, T, s):
    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            return True
        return False


    n = len(G)
    d = bfs(T, s)
    enqueued = [True] * n
    Q = PriorityQueue()

    cnt = 0
    Q.put((d[s], s))
    while not Q.empty() and cnt < n:
        u = Q.get()[1]
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]]:
                if relax(u, v[0], v[1]):
                    return False
                Q.put((d[v[0]], v[0]))
    return True


G = [[(1, 1), (4, 5)],
     [(0, 1), (2, 2), (4, 7)],
     [(1, 2), (3, 3), (4, 3)],
     [(2, 3), (4, 11)],
     [(0, 5), (1, 7), (2, 3), (3, 11), (5, 3), (6, 1)],
     [(4, 3), (6, 5)],
     [(4, 1), (5, 5)]]
T = [[(1, 1)],
     [(0, 1), (2, 2)],
     [(1, 2), (3, 3), (4, 3)],
     [(2, 3)],
     [(2, 3), (5, 3), (6, 1)],
     [(4, 3)],
     [(4, 1)]]
print(spt(G, T, 0))