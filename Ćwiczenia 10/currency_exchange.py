from math import log2

"""Na tablicach w kantorze wisi lista trójek (waluta1, waluta2, kurs). Każda z takich trójek oznacza,
 że kantor kupi n waluty2 za kurs*n waluty1.
 1) Znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B
 2) Czy istnieje taka sekwencja wymiany walut, która zaczyna się i kończy w tej samej walucie i kończymy z większą
    ilością pieniędzy niż zaczynaliśmy?"""

# tworzymy graf, gdzie waluty są wierzchołkami i dla każdych dwóch walut połączonych kursem tworzymy krawędź o wadze
# równej logarytmowi kursu wymiany
# na tym grafie uruchamiamy algorytm Bellmana-Forda, który wyznaczy najkorzystniejszą sekwencję wymiany walut
# jeżeli trafimy na cykl ujemny to znaczy, że istnieje sekwencja z punktu 2)


def path(G, parent, u):
    if parent[u] is None:
        return [u]
    return path(G, parent, parent[u]) + [u]


def bellman_ford(G, s, t):
    n = len(G)
    d = [float("inf")] * n
    parent = [None] * n
    d[s] = 0

    for _ in range(n - 1):
        for i in range(n):
            for j in range(len(G[i])):
                if d[i] != float("inf") and d[i] + G[i][j][1] < d[G[i][j][0]]:
                    d[G[i][j][0]] = d[i] + G[i][j][1]
                    parent[G[i][j][0]] = i

    for i in range(n):
        for j in range(len(G[i])):
            if d[i] != float("inf") and d[i] + G[i][j][1] < d[G[i][j][0]]:
                return None

    route = path(G, parent, t)
    return route


def currency_exchange(T, a, b):
    n = 0
    for i in range(len(T)):
        n = max(n, T[i][0], T[i][1])
    G = [[] for _ in range(n + 1)]
    for i in range(len(T)):
        G[T[i][0]].append((T[i][1], log2(T[i][2])))
    seq = bellman_ford(G, a, b)
    if seq is None:
        return "istnieje sekwencja z punktu 2)"
    return seq


T = [(0, 1, 4.5), (0, 2, 4), (2, 0, 0.25), (1, 2, 0.75), (3, 2, 100), (0, 3, 0.4)]
print(currency_exchange(T, 0, 2))