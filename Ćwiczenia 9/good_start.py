"""Wierzchołek v w grafie skierowanym nazywamy dobrym poczatkiem jesli
kazdy inny wierzchołek mozna osiagnac sciezka skierowana wychodzaca z v. Prosze podac algorytm, który
stwierdza czy dany graf zawiera dobry poczatek."""

# przejdź dfs'em po grafie zapisując czasy przetworzenia wierzchołków, z wierzchołka o największym czasie przetworzenia
# puść dfs'a jeszcze raz, jeżeli uda się wejść do każdego innego wierzchołka to ten wierzchołek jest dobrym początkiem,
# jeżeli nie to graf nie posiada dobrego początku


def dfs_visit(G, visited, u, time=None):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            dfs_visit(G, visited, v, time)
    if time is not None:
        time.append(u)


def good_start(G):
    n = len(G)
    visited = [False] * n
    time = []
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, visited, u, time)
    visited = [False] * n
    dfs_visit(G, visited, time[n - 1])
    for i in range(n):
        if not visited[i]:
            return None
    return time[n - 1]


G = [[1],
     [3],
     [0, 1],
     [4],
     []]
print(good_start(G))