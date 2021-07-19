from queue import PriorityQueue

"""Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N). Proszę zaproponować jak najszybszy
 algorytm, który znajduje ścieżkę z danego wierzchołka s do danego wierzchołka t taką, że:
 1) Każda kolejne krawędź ma mniejszą wagę niż poprzednia
 2) Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wag"""

# w wejściowym grafie dla każdego wierzchołka sortujemy wychodzące z niego krawędzie malejąco, do kolejki priorytetowej
# wrzucamy dodatkowo informację o wadze krawędzi. dokonujemy relaksacji tylko wtedy, gdy waga krawędzi wychodzącej
# z przetwarzanego wierzchołka jest mniejsza od wagi krawędzi wchodzącej do tego wierzchołka


def relax(d, parent, u, v, weight):
    if d[v] > d[u] + weight:
        d[v] = d[u] + weight
        parent[v] = u


def path(parent, u):
    if parent[u] is None:
        return [u]
    return path(parent, parent[u]) + [u]


def monotonic_dijkstra(G, s, t):
    n = len(G)
    d = [float("inf")] * n
    parent = [None] * n
    enqueued = [True] * n
    Q = PriorityQueue()

    for i in range(n):
        G[i].sort(reverse=True, key=lambda x: x[1])

    d[s] = 0
    cnt = 0
    Q.put((d[s], s, float("inf")))
    while not Q.empty() and cnt < n:
        _, u, w = Q.get()
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]] and v[1] < w:
                relax(d, parent, u, v[0], v[1])
                Q.put((d[v[0]], v[0], v[1]))


    route = path(parent, t)
    return route, d[t]


G = [[(1, 9)],
     [(0, 9), (2, 10), (6, 8)],
     [(1, 10), (3, 4)],
     [(2, 4), (4, 5)],
     [(3, 5), (5, 6)],
     [(4, 6), (6, 7)],
     [(2, 8), (5, 7)]]
print(monotonic_dijkstra(G, 0, 2))