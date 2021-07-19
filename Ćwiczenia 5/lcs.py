"""Mamy dane dwie tablice, A[n] i B[n]. Nalezy znalezc
długosc ich najdłuzszego wspólnego podciagu."""

# f(i, j) - długość najdłuższego wspólnego podciąg wykorzystując i pierwszych wyrazów z A oraz j pierwszych wyrazów z B

# f(i, j) = 0 ; i == 0 or j == 0
# f(i, j) = f(i - 1, j - 1) + 1; A[i] == B[j]
# f(i, j) = max(f(i - 1, j), f(i, j - 1)


def lcs(A, B):
    n = len(A)
    F = [[0] * n for _ in range(n)]

    for i in range(n):
        if A[i] == B[0]:
            F[0][i] = 1
        if A[0] == B[i]:
            F[i][0] = 1

    for j in range(1, n):
        for i in range(1, n):
            if A[i] == B[j]:
                F[j][i] = F[j - 1][i - 1] + 1
            else:
                F[j][i] = max(F[j - 1][i], F[j][i - 1])

    return F[n - 1][n - 1]


A = [3, 5, 1, 2, 4, 6, 3, 9]
B = [6, 4, 5, 3, 6, 3, 4, 2]
print(lcs(A, B))