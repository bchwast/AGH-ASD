from queue import Queue

"""Dana jest mapa kraju w postaci grafu G = (V,E). Kierowca chce przejechac
 z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawedzie) sa płatne. Kazda droga ma taką
 samą jednostkowa opłate. Prosze podac algorytm, który znajduje trase wymagajaca jak najmniejszej liczby
 opłat. W ogólnosci graf G jest skierowany, ale mozna najpierw wskazac algorytm dla grafu nieskierowanego."""

# graf w postaci listy sąsiedztwa, gdzie dla każdego wierzchołka mamy listę krotek zawierającą wierzchołek, z którym jest
# połączony krawędzią oraz wagę tej krawędzi

# puszczamy dfs'a


def edges_0_1(G, s, t):
    n = len(G)

    def dfs(G, u):
        if u == t:
            return 0, [u]

        visited[u] = True
        ans = float("inf")
        path = []
        for v in G[u]:
            if not visited[v[0]]:
                cur, cur_p = dfs(G, v[0])

                if cur < float("inf"):
                    if cur < ans:
                        ans = cur + v[1]
                        path = cur_p

        visited[u] = False
        return ans, [u] + path


    visited = [False] * n
    visited[s] = True

    ans, path = dfs(G, s)
    if ans != float("inf"):
        return path


G = [[(1, 0), (2, 1)], [(2, 0), (3, 1)], [(3, 0), (4, 1)], [], [(3, 0)]]
print(edges_0_1(G, 0, 4))