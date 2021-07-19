from queue import Queue

"""W pewnym kraju trwa wojna domowa. W ramach sabotażu rebelianci chcą uniemożliwić komunikację telegraficzną z miasta
 A do B. Otrzymujemy listę miast i linii telegraficznych między nimi. Linie telegraficzne są skierowane. Każda z linii
 ma przypisany koszt zniszczenia jej. Chcemy wybrać zbiór połączeń do zniszczenia o łącznym minimalnym koszcie.
 Interesuje nas nie tylko koszt, ale które konkretnie linie telegraficzne mamy zniszczyć."""

# Tworzymy graf w postaci macierzy, gdzie wierzchołki to miasta, a krawędzie to linie telegraficzne między nimi,
# pojemnościami krawędzi będą koszty zniszczenia danej linii. Uruchamiamy algorytm Edmondsa_Karpa w celu znalezienia
# minimalnego przekroju grafu. Krawędzie wychodzące ze zbioru S do zbioru T to krawędzie o minimalnym łącznym koszcie
# usunięcia


def bfs(G, parent, s, t, mode=0):
    n = len(G)
    visited = [False] * n
    d = [None] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    d[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if not visited[v] and G[u][v] > 0:
                Q.put(v)
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                if v == t and mode == 0:
                    return True
    if mode == 0:
        return False
    return d


def edmonds_karp(G, s, t):
    n = len(G)
    parent = [None] * n
    max_flow = 0

    while bfs(G, parent, s, t):
        path_flow = float("inf")
        s_ = t
        while s_ != s:
            path_flow = min(path_flow, G[parent[s_]][s_])
            s_ = parent[s_]
        max_flow += path_flow

        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]
    return max_flow


def sabotage(cities, lines, a, b):
    n = len(cities)
    G = [[0] * n for _ in range(n)]
    for i in range(len(lines)):
        G[lines[i][0]][lines[i][1]] = lines[i][2]

    _ = edmonds_karp(G, a, b)
    d = bfs(G, [None] * n, a, b, 1)
    m_d = 0
    for i in range(n):
        if d is not None:
            m_d = max(d, m_d)

    res = []
    for i in range(n):
        if d[i] == m_d:
            for j in range(len(lines)):
                if lines[j][0] == i:
                    res.append(lines[j])

    cost = 0
    for i in range(len(res)):
        cost += res[i][2]

    return res, cost