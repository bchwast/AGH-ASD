from queue import PriorityQueue

"""Dany jest graf ważony G. Ścieżka superfajna, to taka, która jest nie tylko najkrótszą wagowo ścieżką między v i u,
 ale także ma najmniejszą liczbę krawędzi (inaczej mówiąc, szukamy najkrótszych ścieżek w sensie liczby krawędzi wśród
 najkrótszych ścieżek w sensie wagowym). Podaj algorytm, który dla danego wierzchołka startowego s znajdzie superfajne
 ścieżki do pozostałych wierzchołków."""

# uruchamiamy algorytm Dijkstry, tylko pamiętamy również o ilości krawędzi na ścieżce


def supercool_paths(G, s, t):
    def relax(u, v, weight):
        if d[v] >= d[u] + weight and l[v] > l[u] + 1:
            d[v] = d[u] + weight
            l[v] = l[u] + 1
            parent[v] = u
        elif d[v] > d[u] + weight:
            d[v] = d[u] + weight
            parent[v] = u

    def path(u):
        if parent[u] is None:
            return [u]
        return path(parent[u]) + [u]


    n = len(G)
    d = [float("inf")] * n
    l = [float("inf")] * n
    parent = [None] * n
    enqueued = [True] * n
    Q = PriorityQueue()

    d[s] = 0
    l[s] = 0
    cnt = 0
    Q.put((d[s], l[s], s))
    while not Q.empty() and cnt < n:
        u = Q.get()[2]
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]]:
                relax(u, v[0], v[1])
                Q.put((d[v[0]], l[v[0]], v[0]))

    route = path(t)
    return route


G = [[(1, 1), (5, 1)],
     [(2, 1)],
     [(3, 1)],
     [(4, 1)],
     [],
     [(4, 3)]]
print(supercool_paths(G, 0, 4))