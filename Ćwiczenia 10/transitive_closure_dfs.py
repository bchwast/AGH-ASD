"""Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować algorytm,
 który oblicza domknięcie przechodnie grafu G (domknięcie przechodnie grafu G to takie graf H, że w H mamy krawędź z
 u do v wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v)."""

# z każdego wierzchołka u w grafie G uruchamiamy DFS i w grafie H dodajemy krawędź z u do każdego wierzchołka v,
# do którego dotarliśmy w G ścieżką zaczynającą się w u


def dfs_visit(G, Hr, visited, u):
    visited[u] = True
    for v in range(len(G)):
        if G[u][v] and not visited[v]:
            Hr[v] = 1
            dfs_visit(G, Hr, visited, v)


def transitive_closure(G):
    n = len(G)
    H = [[0] * n for _ in range(n)]
    for u in range(n):
        visited = [False] * n
        dfs_visit(G, H[u], visited, u)
    return H


G = [[0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]
H = transitive_closure(G)
for i in range(len(H)):
    print(H[i])