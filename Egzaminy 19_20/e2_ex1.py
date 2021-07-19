# 2 pkt

from e2_ex1_testy import runtests


def zbigniew(A):
    n = len(A)
    e_max = sum(A)
    F = [[float("inf")] * (e_max + 1) for _ in range(n)]
    F[0][A[0]] = 0

    for i in range(n):
        for e in range(e_max + 1):
            if F[i][e] != float("inf"):
                for k in range(1, e + 1):
                    if i + k < n and e - k + A[i + k] <= e_max:
                        F[i + k][A[i + k] + e - k] = min(F[i + k][A[i + k] + e - k], F[i][e] + 1)

    res = min(F[n - 1])
    return res


runtests(zbigniew)