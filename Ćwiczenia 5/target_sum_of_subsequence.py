"""Dana jest tablica n liczb naturalnych A. Prosze podac i zaimplementowac
algorytm, który sprawdza, czy da sie wybrac podciag liczb z A, które sumuja sie do zadanej
wartosci T."""

# f(i, j) = {0, 1} - czy można otrzymać sumę j używając i pierwszych liczb z A

# f(i, 0) = 1
# f(i ,j) = f(i - 1, j) or f(i - 1, j - A[i - 1])


def tssum(T, target):
    n = len(T)
    F = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        F[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < T[i - 1]:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = (F[i - 1][j] or F[i - 1][j - T[i - 1]])

    return F[n][target]




T = [3, 34, 4, 12, 5, 2]
print(tssum(T, 13))