# Bartłomiej Chwast

from math import *


def distance(a, b):
    # funkcja zwracająca odległość pomiędzy dwoma punktami (czysta estetyka)
    return sqrt(((a[1] - b[1]) * (a[1] - b[1])) + ((a[2] - b[2]) * (a[2] - b[2])))


def get_path(C, path, i, j, n):
    # funkcja odtwarzajaca przebieg trasy, (przepis, punkty pomiędzy i pozostała ilość punktów)

    # warunek końca rekurencji, początek budowania trasy
    if n <= 0:
        return []

    if i <= j:
        # dokładamy punkt z lewej strony
        k = path[i][j]
        return [C[k][0]] + get_path(C, path, k, j, n - 1)
    else:
        # dokładamy punkt z prawej strony
        k = path[j][i]
        return get_path(C, path, i, k, n - 1) + [C[k][0]]


def bitonic_tsp(C):
    # funkcja znajdująca optymalną trasę w postaci iteracyjnej
    n = len(C)

    # sortujemy punkty względem x-owej wspołrzędnej
    C.sort(key=lambda x: x[1])

    # tworzymy tablicę zawierającą odległości pomiędzymi poszczególnymi parami miast
    D = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            D[i][j] = distance(C[i], C[j])

    # tworzymy tablicę F[i][j], w której algorytm będzie umieszczał optymalne długości tras rozpoczynających się w i,
    # kończących się w j (i < j) zawierających wszystkie punkty od i do n - 1
    F = [[float("inf")] * n for _ in range(n)]

    # tworzymy tablicę, w której będziemy umieszczać punkty do późniejszego odtworzenia trasy
    path = [[None] * n for _ in range(n)]

    # warunki początkowe
    F[n - 2][n - 1] = D[n - 2][n - 1]
    path[n - 2][n - 1] = n - 1

    # przechodzimy po punktach od końca
    for i in range(n - 3, -1, -1):
        minimal = float("inf")

        # szukamy minimalnego kosztu trasy, gdy punkty i oraz k są na jednej ścieżce (i + 1 < k <= n - 1), a punkty od
        # i + 1 do k - 1 na drugiej
        for k in range(i + 2, n):
            if minimal > F[i + 1][k] + D[i][k]:
                minimal = F[i + 1][k] + D[i][k]
                mink = k
        F[i][i + 1] = minimal
        # zapamiętujemy k, dla którego otrzymaliśmy minimalny koszt
        path[i][i + 1] = mink

        # szukamy minimalnego kosztu trasy, gdy punkty od i do j - 1 są na jednej ścieżce, a j na drugiej (i + 1 < j)
        for j in range(i + 2, n):
            F[i][j] = F[i + 1][j] + D[i][i + 1]
            # zapamiętujemy i + 1
            path[i][j] = i + 1

    # kończymy trasę łącząc punkt startowy z najbliższym
    F[0][0] = F[0][1] + D[0][1]
    path[0][0] = 1

    # odtwarzamy trasę
    route = get_path(C, path, 0, 0, n - 1)

    # zwracamy koszt optymalnej trasy i jej przebieg
    return F[0][0], route


def bitonicTSP(C):
    # wywołujemy właściwe funkcje
    result, route = bitonic_tsp(C)

    # wypisujemy trasę
    print(C[0][0], *route, C[0][0], sep=",")

    # zwracamy długość
    return result


# C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1], ["paprykarz szczecinski", 1, 3]]
# bitonicTSP(C)
# C = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
#      ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
#      ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]
# print(bitonicTSP(C))
