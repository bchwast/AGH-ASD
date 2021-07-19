from queue import Queue

"""Dany jest graf G = (V,E), gdzie kazda krawedz ma wage ze zbioru
 {1, . . . , |E|} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych wierzchołków
 x i y sprawdza, czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o coraz mniejszych wagach."""

# graf w postaci listy sąsiedztwa, gdzie dla każdego wierzchołka mamy listę krotek zawierającą wierzchołek, z którym jest
# połączony krawędzią oraz wagę tej krawędzi

# z wierzchołka x odpalamy bfs'a i przechodzimy tylko po krawędziach o mniejszej wadze, możemy odwiedzać wierzchołki
# kilka razy, jak dotrzemy do y zwracamy True, jak nie to False


def decreasing_edges(G, x, y):
    Q = Queue()
    Q.put((x, float("inf")))

    while not Q.empty():
        u = Q.get()
        if u[0] == y:
            return True

        for v in G[u[0]]:
            if v[1] < u[1]:
                Q.put((v[0], v[1]))

    return False


G = [[(1, 13), (2, 10), (5, 3)], [(0, 13), (2, 12)], [(0, 10), (3, 3), (4, 11)], [(2, 3), (4, 5)], [(2, 11), (3, 5), (5, 5)],
     [(0, 3), (4, 5)]]
print(decreasing_edges(G, 0, 4))