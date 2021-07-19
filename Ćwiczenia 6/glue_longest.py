"""Dany jest ciag przedziałów postaci [ai, bi]. Dwa przedziały mozna
skleic jesli maja dokładnie jeden punkt wspólny. Prosze wskazac algorytmy dla nastepujacych problemów:

Problem stwierdzenia jaki najdłuzszy odcinek mozna uzyskac sklejajac najwyzej k odcinków."""

# f(i, j) - minimalna liczba przedziałów, które trzeba skleić, żeby powstał przedział od i do j

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


def glue_ranges(A, k):
    a = beg_b = float("inf")
    b = end_a = float("-inf")

    for i in range(len(A)):
        a = min(a, A[i][0])
        end_a = max(end_a, A[i][0])
        b = max(b, A[i][1])
        beg_b = min(beg_b, A[i][1])

    n = b - a + 1
    F = [[None] * n for _ in range(n)]

    for i in range(len(A)):
        F[A[i][0] - a][A[i][1] - a] = 1

    res = float("-inf")
    for i in range(a, end_a + 1):
        for j in range(beg_b, b + 1):
            glue(A, F, i, j, a)
            if F[i - a][j - a] and F[i - a][j - a] <= k:
                res = max(res, j - i + 1)

    return res


A = [(1, 4), (5, 7), (4, 6), (8, 9), (6, 8), (7, 10)]

print(glue_ranges(A, 2))