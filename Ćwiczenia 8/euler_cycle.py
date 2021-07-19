# Bartłomiej Chwast

from copy import deepcopy

# główna funkcja do szukania cyklu Eulera
def euler(G):
    # realizacja dfs (graf, parent obecnego wierzchołka, obecny wierzchołek)
    def dfs(graph, u, v):
        # zapisujemy, że odwiedziliśmy dany wierzchołek (w celu sprawdzenia spójności później)
        visited[v] = True
        # usuwamy krawędź pomiędzy obecnym wierzchołkiem a parentem w obie strony
        if u != v:
            graph[u][v] = 0
            graph[v][u] = 0

        # szukamy krawędzi wychodzących z obecnego wierzchołka, zaczynając od tego, na którym skończyliśmy przy ostatniej
        # wizycie w obecnym wierzchołku
        for i in range(vert[v] + 1, n):
            vert[v] += 1
            # jeżeli krawędź istnieje to przechodzimy dalej dfs'em
            if graph[v][i]:
                dfs(graph, v, i)
        # po przetworzeniu dodajemy obecny wierzchołek do listy
        cycle.append(v)

    n = len(G)
    # visited do późniejszego sprawdzenia spójności
    visited = [False] * n
    # vert do zapamiętania, której ostatniej krawędzi wychodzącej z danego wierzchołka szukaliśmy
    vert = [-1] * n
    # kopiujemy graf, żeby go nie niszczyć
    graph = [[G[i][j] for j in range(n)] for i in range(n)]
    # tu będziemy zapisywać nasz cykl
    cycle = []

    # sprawdzamy czy każdy wierzchołek ma parzysty stopień
    for u in range(n):
        cnt = 0
        for v in range(n):
            if G[u][v]:
                cnt += 1
        if cnt % 2 != 0:
            return None
    # wywołujemy dfs'a w pierwszym wierzchołku
    dfs(graph, 0, 0)

    # sprawdzamy spójność grafu
    for i in range(n):
        if not visited[i]:
            return None
    # zwracamy cykl
    return cycle


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = deepcopy(G)
cycle = euler(G)
print(cycle)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
