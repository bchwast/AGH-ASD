"""Dany jest cieg macierzy A1,A2, . . . ,An. Ktos chce policzyc iloczyn
A1A2...An. Macierze nie sa koniecznie kwadratowe (ale oczywiscie znamy ich rozmiary). Zaleznie w jakiej
kolejnosci wykonujemy mnozenia, koszt obliczeniowy moze byc rózny—nalezy podac algorytm znajdujacy
koszt mnozenia przy optymalnym doborze kolejnosci."""

# f(i, j) - minimalny koszt mnożenia macierzy od i do j

# f(i, j) = 0 ; i == j
# f(i, j) = min(f(i, k) + f(k + 1, j) + dim(i - 1)*dim(k)*dim(j)) ; i <= k < j


def print_solution(best, low, high):
    if high == low:
        print(f"F[{high}]", end="")
    else:
        print("(", end="")
        print_solution(best, low, best[low][high])
        print_solution(best, best[low][high] + 1, high)
        print(")", end="")


def matrix_multiply(M):
    n = len(M)
    F = [[None] * (n) for _ in range(n)]
    best = [[None] * (n) for _ in range(n)]

    for i in range(1, n):
        F[i][i] = 0

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            F[i][j] = float("inf")
            for k in range(i, j):
                cost = F[i][k] + F[k + 1][j] + (M[i - 1] * M[k] * M[j])
                if cost < F[i][j]:
                    F[i][j] = cost
                    best[i][j] = k

    return F[1][n - 1], best


M = [40, 20, 30, 10, 30]
res, best = matrix_multiply(M)
print(res)
print_solution(best, 1, len(M) - 1)