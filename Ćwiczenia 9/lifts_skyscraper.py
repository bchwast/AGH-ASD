"""Wieżowiec ma 100 pięter i n wind, nie ma natomiast schodów. Każda winda posiada listę pięter,
 do których dojeżdża i prędkość w sekundach na piętro.
 Jesteśmy na piętrze i, chcemy się dostać na piętro j. Ile minimalnie sekund musimy spędzić w windach, aby tam dotrzeć?"""

# tworzymy graf, gdzie wierzchołkami będą piętra, na które będziemy się mogli dostać poszczególnymi windami
# krawędziami o wadze czasu przejazdu łączymy wierzchołki z poszczególnej windy, a wierzchołki na jednym piętrze łączymy
# krawędziami o wadze 0
# uruchamiamy algorytm Dijkstry z dowolnego wierzchołka na i-tym piętrze i zwracamy koszt czasowy dotarcia do dowolnego
# wierzchołka na j-tym piętrze
# tylko jak to sensownie zaimplementować? XD

# tworzymy graf o 101 wierzchołkach będących piętrami i krawędziach o wagach będących minimalnymi czasami bezpośredniego
# przejazdu pomiędzy danymi piętrami, graf w postaci macierzowej
# uruchamiamy algorytm Dijkstry z i-tego wierzchołka i zwracamy koszt czasowy dotarcia do j-tego wierzchołka


def min_d(d, enqueued, n):
    best = float("inf")
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def dijkstra(G, s, t):
    n = len(G)
    d = [(float("inf"))] * n
    enqueued = [True] * n

    d[s] = 0
    for i in range(n):
        if not enqueued[t]:
            break
        u = min_d(d, enqueued, n)
        enqueued[u] = False

        for v in range(n):
            if 0 <= G[u][v] and d[u] + G[u][v] < d[v] and enqueued[v]:
                d[v] = G[u][v] + d[u]

    return d[t]


def skyscraper(lifts, i, j):
    n = len(lifts)
    G = [[float("inf") for _ in range(101)] for _ in range(101)]
    for a in range(n):
        for b in range(len(lifts[a][0]) - 1):
            G[lifts[a][0][b]][lifts[a][0][b + 1]] = min(G[lifts[a][0][b]][lifts[a][0][b + 1]], (lifts[a][0][b + 1] -
                                                                                        lifts[a][0][b]) * lifts[a][1])
            G[lifts[a][0][b + 1]][lifts[a][0][b]] = G[lifts[a][0][b]][lifts[a][0][b + 1]]

    return dijkstra(G, i, j)


lifts = [([1, 2, 5], 1), ([0, 3, 5], 2), ([0, 3], 2), ([1, 2, 4], 3), ([3, 5], 1), ([0, 1, 2, 3, 4, 5], 5)]
print(skyscraper(lifts, 0, 5))
