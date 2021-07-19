from queue import Queue

"""W kafejce internetowej jest K komputerów i A aplikacji na płytach CD. Na każdym komputerze może być zainstalowana
 maksymalnie jedna aplikacja. Każda aplikacja ma listę komputerów na których może działać, a na pozostałych nie może
 z powodu wymagań sprzętowych. Jesteś właścicielem kafejki i wiesz, ilu klientów (możliwie zero) będzie chciało jutro
 skorzystać z danej aplikacji. Zakładamy, że każdy klient zajmuje komputer na cały dzień.
 Jaką aplikację powinieneś zainstalować na każdym z komputerów, aby wszyscy klienci mogli skorzystać z tej aplikacji,
 którą chcą? Jeżeli takie przyporządkowanie nie istnieje, algorytm powinien to stwierdzić."""

# Tworzymy graf dwudzielny, gdzie wierzchołki z "lewego" zbioru to aplikacje, a wierzchołki z "prawego" to komputery
# aplikacje łączymy z kompatybilnymi komputerami krawędziami o pojemności 1. Tworzymy superźródłom które łączymy z
# aplikacjami krawędziami o pojemności równej ilości klientów chcących korzystać z danej aplikacji. Tworzymy również
# superujście, które łączymy z komputerami krawędziami o pojemności 1. Uruchamiamy algorytm Edmondsa-Karpa,
# jeżeli wartość maksymalnego przepływu będzie równa łącznemu zapotrzebowaniu na korzystanie z aplikacji to takie
# przyporządkowanie istnieje, jeżeli jest mniejsza to nie istnieje


def bfs(G, parent, s, t):
    n = len(G)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if not visited[v] and G[u][v] > 0:
                Q.put(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False


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


def internet_cafe(A, K, apps, customers):
    n = A + K + 2
    G = [[0] * n for _ in range(n)]
    demand = 0
    for i in range(len(apps)):
        for j in range(len(apps[i])):
            G[i][A + apps[i][j]] = 1
    for i in range(len(customers)):
        G[n - 2][i] = customers[i]
        demand += customers[i]
    for i in range(K):
        G[A + i][n - 1] = 1

    res = edmonds_karp(G, n - 2, n- 1)
    if res == demand:
        return True
    return False
