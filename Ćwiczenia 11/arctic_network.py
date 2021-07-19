from math import sqrt, ceil

"""W Arktyce osady są oddalone od siebie na ogromne odległości. Otrzymujemy je jako pary współrzędnych (x, y).
 Niektóre z nich posiadają odbiorniki satelitarne - z takiej osady można bezpośrednio komunikować się z każdą inną
 osadą, która ma odbiornik satelitarny. Chcemy teraz w każdej osadzie umiejscowić radioodbiorniki o tym samym
 ograniczonym zasięgu D (liczba całkowita), aby można było się komunikować (pośrednio lub bezpośrednio) między każdą
 parą osad. Jakie jest minimalne D, które pozwoli osiągnąć ten cel? Uzasadnij poprawność rozwiązania."""

# Tworzymy graf w postaci listy krawędzi, gdzie krawędzie występują pomiędzy każdą parą osad, a wagami jest odległość
# euklidesowa pomiędzy nimi. Następnie sortujemy te krawędzie niemalejąco po wagach, każdy wierzchołek wzucamy do
# osobnego zbioru rozłącznego, wierzchołki posiadające odbiorniki satelitarne łączymy w jeden zbiór.
# Uruchamiamy algorytm Kruskala i znajdujemy MST, sufit z krawędzi o największej wadze to szukane minimalne D


class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


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


def kruskal(G, v):
    G.sort(key=lambda x: x[2])
    A = []

    for e in G:
        if find(v[e[0]]) != find(v[e[1]]):
            A.append(e)
            union(v[e[0]], v[e[1]])

    return A


def arctic_network(camps, sats):
    n = (len(camps) * (len(camps) - 1)) // 2
    G = [None] * n
    ind = 0
    for i in range(len(camps)):
        for j in range(i + 1, len(camps)):
            G[ind] = (i, j, sqrt((camps[i][0] - camps[j][0]) ** 2 + (camps[i][1] - camps[j][1]) ** 2))
            ind += 1

    v = [Node(i) for i in range(n)]
    for i in range(1, len(sats)):
        union(v[sats[0]], v[sats[i]])
    mst = kruskal(G, v)
    D = mst[len(mst) - 1][2]
    return D
