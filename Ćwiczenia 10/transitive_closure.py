"""Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować algorytm,
 który oblicza domknięcie przechodnie grafu G (domknięcie przechodnie grafu G to takie graf H, że w H mamy krawędź z
 u do v wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v)."""

# modyfikujemy algorytm Floyda-Warshalla, zamiast trzymać w macierzy długość ścieżki, trzymamy informację czy dany
# wierzchołek jest osiągalny. operacje arytmetyczne zastępujemy operacjami logicznymi


def transitive_closure(G):
    n = len(G)
    H = [i[:] for i in G]

    for t in range(n):
        for u in range(n):
            for w in range(n):
                H[u][w] = H[u][w] or (H[u][t] and H[t][w])

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