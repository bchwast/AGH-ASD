"""Wyobraźmy sobie podziemny labirynt, złożony z ogromnych jaskiń połączonych wąskimi korytarzami. W jednej z jaskiń
 krasnoludy zbudowały swoją osadę, a w każdej z pozostałych jaskiń mieszka znana krasnoludom ilość trolli.
 Krasnoludy chcą zaplanować swoją obronę na wypadek ataku ze strony trolli.
 Zamierzają w tym celu zakraść się i podłożyć ładunek wybuchowy pod jeden z korytarzy, tak aby trolle mieszkające za
 tym korytarzem nie miały żadnej ścieżki, którą mogłyby dotrzeć do osady krasnoludów.
 Który korytarz należy wysadzić w powietrze, aby odciąć dostęp do krasnoludzkiej osady największej liczbie trolli?
"""

# zapisujemy ile trolli znajduje się w wierzchołku i jego dzieciach, szukamy mostu, którego usunięcie zabierze nam
# najwięcej trolli


def dwarves_trolls(G, trolls):
    n = len(G)
    time = 0

    def dfs(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        d[u] = time
        low[u] = time
        all_trolls[u] = trolls[u]

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs(G, v)
                low[u] = min(low[u], low[v])
                all_trolls[u] += all_trolls[v]
            elif parent[u] != v:
                low[u] = min(low[u], low[v])


    visited = [False] * n
    d = [None] * n
    low = [None] * n
    parent = [None] * n
    all_trolls = [0] * n

    for u in range(n):
        if not visited[u]:
            dfs(G, u)
    all_trolls[0] = 0

    res = []
    for u in range(n):
        if d[u] == low[u] and parent[u] is not None:
            res.append((parent[u], u))
    fin = 0

    for u in res:
        if all_trolls[u[1]] > all_trolls[fin]:
            fin = u[1]

    return fin


G = [[1, 7], [0, 2, 7], [1, 3, 5], [2, 4, 5], [3], [2, 3, 6], [5], [0, 1, 8], [7]]
trolls = [0, 13, 5, 3, 1, 5, 2, 2, 7]
print(dwarves_trolls(G, trolls))