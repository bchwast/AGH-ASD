"""Dany jest ciag przedziałów postaci [ai, bi]. Dwa przedziały mozna
skleic jesli maja dokładnie jeden punkt wspólny. Prosze wskazac algorytmy dla nastepujacych problemów:

Problem stwierdzenia, czy da sie uzyskac przedział [a, b] przez sklejanie odcinków, ale kazdy odcinek ma koszt
i pytamy o minimalny koszt uzyskania odcinka [a, b]."""

# f(i, j) - minimalny koszt uzyskania przedział od i do j

# f(i, j) = False - nie da się uzyskać przedziału od i do j
# f(i, j) = min(f(i, k) + f(k, j)) ; i < k < j; jeżeli f(i, k) != False && f(k, j) != False


def glue(A, F, i, j, a):
    if F[i - a][j - a] != None:
        return F[i - a][j - a]

    F[i - a][j - a] = float("inf")
    for k in range(i + 1, j):
        F[i - a][k - a] = glue(A, F, i, k, a)
        F[k - a][j - a] = glue(A, F, k, j, a)
        if F[i - a][k - a] and F[k - a][j - a]:
            F[i - a][j - a] = min(F[i - a][j - a], F[i - a][k - a] + F[k - a][j - a])

    if F[i - a][j - a] == float("inf"):
        F[i - a][j - a] = False
    return F[i - a][j - a]


def glue_ranges(A, a, b):
    n = b - a + 1
    F = [[None] * n for _ in range(n)]

    for i in range(len(A)):
        if A[i][0] >= a and A[i][1] <= b:
            F[A[i][0] - a][A[i][1] - a] = A[i][2]

    return glue(A, F, a, b, a)


A = [(1, 4, 5), (5, 7, 3), (4, 6, 10), (8, 9, 18), (6, 8, 9), (7, 10, 7), (7, 8, 1), (8, 10, 1)]

print(glue_ranges(A, 5, 10))