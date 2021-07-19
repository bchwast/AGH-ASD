"""Dana jest posortowana tablica A zawierajaca n liczb i celem jest wyznaczenie
liczby x takiej, ze wartosc sum(i = 0, n - 1)|A[i] − x| jest minimalna. Prosze zaproponowac algorytm, uzasadnic
jego poprawnosc oraz ocenic złozonosc obliczeniowa."""

# wystarczy zwrócić medianę


def sum_of_distances(A):
    n = len(A)
    if n % 2 == 1:
        return A[(n - 1) // 2]
    return (A[(n - 1) // 2] + A[((n - 1) // 2) + 1]) / 2