"""Black Forest to las rosnacy na osi liczbowej gdzies w południowej Anglii. Las
składa sie z n drzew rosnacych na pozycjach 0, . . . ,n−1. Dla kazdego i > {0, . . . ,n−1} znany jest zysk ci, jaki
mozna osiagnac scinajac drzewo z pozycji i. John Lovenoses chce uzyskac maksymalny zysk ze scinanych
drzew, ale prawo zabrania scinania dwóch drzew pod rzad. Prosze zaproponowac algorytm, dzieki któremu
John znajdzie optymalny plan wycinki"""

# f(i) - maksymalny zysk ze ścięcia drzew od 0 do i

# f(0) = c[0]
# f(1) = max(c[0], c[1])
# f(i) = max(f(i - 2) + c[i], f(i - 1)); i >= 2


def black_forest(C):
    F = [-1] * len(C)
    F[0] = C[0]
    F[1] = max(C[0], C[1])

    for i in range(2, len(C)):
        F[i] = max(F[i - 2] + C[i], F[i - 1])

    return F[len(C) - 1]


T = [4, 2, 5, 10 ,5]
print(black_forest(T))