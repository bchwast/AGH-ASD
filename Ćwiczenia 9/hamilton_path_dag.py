"""Sciezka Hamiltona to sciezka przechodzaca przez wszystkie
wierzchołki w grafie, przez kazdy dokładnie raz. W ogólnym grafie znalezienie sciezki Hamiltona jest problemem
NP-trudnym. Prosze podac algorytm, który stwierdzi czy istnieje sciezka Hamiltona w acyklicznym
grafie skierowanym."""

# posortuj topologicznie DAG, następnie sprawdź czy po między każdą kolejną parą wierzchołków istnieje krawędź. jeżeli
# tak to badany graf posiada ścieżkę Hamiltona, jeżeli nie to nie


def dfs_visit(G, visited, utility, u, mode):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            if mode == "path":
                utility[v] = u
            dfs_visit(G, visited, utility, v, mode)
    if mode == "top":
        utility.append(u)


def hamilton_path_dag(G):
    n = len(G)
    visited = [False] * n
    res = []
    for u in range(n):
        if not visited[u]:
            dfs_visit(G, visited, res, u, "top")
    res.reverse()

    visited = [False] * n
    parent = [None] * n
    dfs_visit(G, visited, parent, res[0], "path")
    for i in range(1, n):
        if parent[res[i]] is None:
            return False
    return True

G = [[1, 2],
     [2],
     [],
     [1]]
print(hamilton_path_dag(G))
