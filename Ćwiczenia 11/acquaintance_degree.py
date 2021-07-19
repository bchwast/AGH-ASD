from queue import Queue

"""Definiujemy relację znajomości między osobami jako symetryczną.
 Znajomość:
 - pierwszego stopnia to bezpośrednia znajomość osoby
 - drugiego stopnia to bycie “znajomym znajomego” osoby, ale nie bezpośrednim znajomym osoby trzeciego, czwartego,
   piątego stopnia, itd.
 - nieskończonego stopnia zachodzi wtedy gdy nie ma ciągu znajomości, który łączyłby dwie osoby
 Mając na wejściu listę osób i znajomości pierwszego stopnia między nimi, chcemy znaleźć największy stopień znajomości
 wśród każdej z możliwych par.
 Znajdź optymalne rozwiązanie zarówno dla grafów rzadkich (|E| = O(|V|)), jak i gęstych (|E| = O(|V|^2)"""

# Sprawdzamy spójność grafu, jeżeli graf nie jest spójny to największy stopień znajomości wynosi nieskonczoność
# Szukamy najdłuższej z najkrótszych ścieżek pomiędzy wszystkimi wierzchołkami
# Dla grafów rzadkich wystarczy V razy puścić BFS'a
# Dla grafów gęstych można V razy puścić BFS'a lub użyć algorytmu Floyda-Warshalla, tu użyjemy BFS'a


def bfs(G, s):
    n = len(G)
    visited = [False] * n
    dist = [float("inf")] * n
    Q = Queue()

    Q.put(s)
    visited[s] = True
    dist[s] = 0
    while not Q.empty():
        u = Q.put()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                Q.put(v)
    return max(dist)


def acquaintance_degree(people, acquaintances):
    n = len(people)
    G = [[] for _ in range(n)]
    for i in range(len(acquaintances)):
        G[acquaintances[i][0]].append(acquaintances[i][1])
        G[acquaintances[i][1]].append(acquaintances[i][0])

    res = bfs(G, 0)
    if res == float("inf"):
        return res
    for i in range(1, n):
        res = max(res, bfs(G, i))
    return res