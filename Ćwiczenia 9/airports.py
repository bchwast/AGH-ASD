"""Dostajemy na wejściu listę trójek (miastoA, miastoB, koszt). Każda z nich oznacza, że możemy zbudować drogę między
 miastem A i B za podany koszt. Ponadto, w dowolnym mieście możemy zbudować lotnisko za koszt K, niezależny od miasta.
 Na początku w żadnym mieście nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
 Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde miasto miało dostęp do lotniska.
 Miasto ma dostęp do lotniska, jeśli:
 1) jest w nim lotnisko, lub
 2) można z niego dojechać do innego miasta, w którym jest lotnisko
 Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z największą ilością lotnisk.
"""

# uruchamiamy algorytm Kruskala na na krawędziach z kosztami < K, następnie w każdym ze zbiorów rozłącznych budujemy
# jedno lotnisko


class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self
        self.done = False


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def airports(G, K):
    G.sort(key=lambda x: x[2])
    n = 0
    for i in range(len(G)):
        n = max(n, G[i][0], G[i][1])
    n += 1

    v = [Node(i) for i in range(n)]
    roads = []

    for e in G:
        if e[2] >= K:
            break
        if find(v[e[0]]) != find(v[e[1]]):
            roads.append((e[0], e[1]))
            union(v[e[0]], v[e[1]])

    ports = []
    for dset in v:
        if not dset.parent.done:
            ports.append(dset.val)
            dset.parent.done = True

    return roads, ports


G = [(0, 1, 2), (1, 2, 7), (2, 3, 6), (2, 4, 6), (2, 5, 5), (1, 5, 8), (1, 6, 4), (0, 6, 3), (5, 6, 9),
     (1, 0, 2), (2, 1, 7), (3, 2, 6), (4, 2, 6), (5, 2, 5), (5, 1, 8), (6, 1, 4), (6, 0, 3), (6, 5, 9)]
print(airports(G, 6))