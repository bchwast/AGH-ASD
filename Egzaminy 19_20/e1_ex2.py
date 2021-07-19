from e1_ex2_testy import runtests


def sumpr(low, high, pref):
    return pref[high + 1] - pref[low]


def opt_sum(T):
    n = len(T)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + T[i]

    F = [[float("-inf")] * n for _ in range(n)]
    for i in range(1, n):
        F[i - 1][i] = abs(sumpr(i - 1, i, pref))

    for j in range(2, n):
        for i in range(j - 1, -1, -1):
            F[i][j] = max(abs(sumpr(i, j, pref)), min(F[i][j - 1], F[i + 1][j]))

    return F[0][n - 1]



runtests( opt_sum )
