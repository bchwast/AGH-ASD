"""Prosze podac algorytm, który majac na wejsciu drzewo oblicza
skojarzenie o maksymalnej licznosci. Czy algorytm dalej bedzie działac jesli kazda krawedz bedzie miec
dodatnia wage i szukamy skojarzenia o maksymalnej sumie wag?"""

# f(x) - maksymalne skojarzenie dla drzewa o korzeniu w x
# g(x) - maksymalne skojarzenie dla drzewa o korzeniu w x bez wykorzystania krawędzi wychodzących z x

# g(x) = sum(f(y)) ; y - dziecko x
# f(x) = g(x) + max(g(y) - f(y) + w(x, y), 0) ; y - dziecko x, w - waga krawędzi


def f(T, F, G, x):
    if F[x] is not None:
        return F[x]
    if F[x] == []:
        F[x] = 0
        return 0
    res = g(T, F, G, x)
    m = 0
    for y in T[x]:
        m = max(m, g(T, F, G, y[0]) - f(T, F, G, y[0]) + y[1])
    res += m
    F[x] = res
    return res


def g(T, F, G, x):
    if G[x] is not None:
        return G[x]
    if T[x] == []:
        G[x] = 0
        return 0
    res = 0
    for y in T[x]:
        res += f(T, F, G, y[0])
    G[x] = res
    return res


def tree_matching(T, root):
    n = len(T)
    F = [None] * n
    G = [None] * n
    return f(T, F, G, root)


T = [[(1, 1), (2, 1)],
     [(3, 1)],
     [],
     []]
print(tree_matching(T, 0))