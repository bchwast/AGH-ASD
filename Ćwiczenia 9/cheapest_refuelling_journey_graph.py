from queue import PriorityQueue

"""Dostajemy na wejściu graf, w którym wierzchołkami są miasta, a krawędziami drogi między nimi.
 Dla każdego miasta znamy cenę paliwa w złotych na litr, a dla każdej drogi jej długość w kilometrach.
 Nasz samochód ma zbiornik pojemności 100 litrów i pali jeden litr na kilometr.
 Startujemy z miasta A z pustym zbiornikiem. Ile minimalnie musimy zapłacić za paliwo, aby dotrzeć do miasta B?
"""

# każdy wierzchołek rozdzielamy na 100 wierzchołków zawierających informację z jaką ilością paliwa do niego dotarliśmy
# każdy z tych wierzchołków łączymy krawędziami z wierzchołkami do których możemy dotrzeć, wagą takiej krawędzi będzie
# koszt paliwa, które musimy zatankować w danym wierzchołku, z którego wychodzimy


def dijkstra(G, s, t):
    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight
            parent[v] = u

    def path(u):
        if parent[u] is None:
            return [u]
        return path(parent[u]) + [u]


    n = len(G)
    d = [float("inf")] * n
    parent = [None] * n
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

    route = path(t)
    return d[t], route


def refuelling(G, s, t):
    n = len(G)
    big_G = [[] for _ in range(100 * n)]
    for i in range(n):
        for j in range(len(G[i])):
            for k in range(i * 100, (i + 1) * 100):
                for l in range(G[i][j][0] * 100, (G[i][j][0] + 1) * 100):
                    if 0 <= l % 100 - k % 100 < 100:
                        big_G[k].append((l, G[i][j][1] * (l % 100 - k % 100)))

    # for i in range(n * 100):
    #     print(big_G[i])

    ind = 0
    min_val = float("inf")
    res = None
    for i in range(t * 100, (t + 1) * 100):
        val, route = dijkstra(big_G, s * 100, i)
        if val < min_val:
            min_val = val
            res = route
        ind += 1

    for i in range(len(res)):
        res[i] //= 100
    return res


G = [[(1, 1), (4, 5)],
     [(0, 1), (2, 7), (3, 8), (4, 2)],
     [(1, 7), (3, 1)],
     [(2, 1), (1, 8), (4, 3)],
     [(0, 5), (1, 2), (3, 3)]]
print(refuelling(G, 0, 4))