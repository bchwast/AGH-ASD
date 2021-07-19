from queue import PriorityQueue

"""Dany jest graf ważony z dodatnimi wagami G. Dana jest też lista E’ krawędzi, które nie należą do grafu,
 ale są krawędziami między wierzchołkami z G. Dane są również dwa wierzchołki s i t. Podaj algorytm, który stwierdzi,
 którą jedną krawędź z E’ należy wszczepić do G, aby jak najbardziej zmniejszyć dystans między s i t.
 Jeżeli żadna krawędź nie poprawi dystansu między s i t, to algorytm powinien to stwierdzić."""

# puszczamy Dijkstrę z wierzchołka s i w tablicy d_s zapisujemy odległości do poszczególnych wierzchołków
# odwracamy krawędzie i puszczamy Dijkstrę z wierzchołka t, zapisując w tablicy d_t odległości do poszczególnych
# wierzchołków, następnie dla każdej krawędzi z E' (postaci (u, v, w)) sprawdzamy czy d_s[u] + d_t[v] + w jest
# mniejsze od d_s[t], jeżeli tak to szukamy takiej krawędzi, która da nam najmniejszą odległość


def dijkstra(G, s):
    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight


    n = len(G)
    d = [float("inf")] * n
    enqueued = [True] * n
    Q = PriorityQueue()

    d[s] = 0
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
                relax(u, v[0], v[1])
                Q.put((d[v[0]], v[0]))

    return d


def edge_decreasing_distance(G, E_, s, t):
    n = len(G)
    d_s = dijkstra(G, s)
    rev_G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            rev_G[G[i][j][0]].append((i, G[i][j][1]))
    d_t = dijkstra(rev_G, t)

    min_e, min_d = None, d_s[t]
    for i in range(len(E_)):
        u, v, w = E_[i]
        if d_s[u] + d_t[v] + w < min_d:
            min_d = d_s[u] + d_t[v] + w
            min_e = i

    if min_e is None:
        return None
    return E_[min_e]


G = [[(1, 10), (3, 5)],
     [(2, 10)],
     [(3, 2)],
     []]
E_ = [(0, 2, 2)]
print(edge_decreasing_distance(G, E_, 0, 3))