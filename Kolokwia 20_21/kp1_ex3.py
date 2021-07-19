# 2 pkt

# f(i, j) - najmniejsza liczba tankowań potrzebnych, żeby dotrzeć do i-tej stacji mając na niej j litrów paliwa w baku

# f(i, j) = inf     ; j > q or j < 0
# f(0, j) = 1       ; j <= V[0]
# f(0, j) = inf     ; j > V[0]
# f(i, j) = min(f(i - k, max(0, j - V[i]) + (T[i] - T[i - k]))

from kp1_ex3_testy import runtests


def late(F, i, j, T, V, q, P):
    if j > q:
        return float("inf")
    if F[i][j] is not None:
        return F[i][j]

    F[i][j] = float("inf")
    for k in range(i - 1, -1, -1):
        tmp = late(F, k, max(0, j - V[i]) + (T[i] - T[k]), T, V, q, P) + 1
        if tmp < F[i][j]:
            F[i][j] = tmp
            P[i][j] = (k, max(0, j - V[i]) + (T[i] - T[k]))
    return F[i][j]


def get_solution(P, i, j):
    if P[i][j] is None:
        return [i]
    return get_solution(P, P[i][j][0], P[i][j][1]) + [i]


def iamlate(T, V, q, l):
    T.append(l)
    V.append(0)
    n = len(T)
    F = [[None] * (q + 1) for _ in range(n)]
    P = [[None] * (q + 1) for _ in range(n)]

    for j in range(q + 1):
        if j > V[0]:
            F[0][j] = float("inf")
        else:
            F[0][j] = 1

    for j in range(q + 1):
        _ = late(F, n - 1, j, T, V, q, P)

    best = float("inf")
    bj = None
    for j in range(q + 1):
        if F[n - 1][j] < best:
            best = F[n - 1][j]
            bj = j

    if best == float("inf"):
        return []
    sol = get_solution(P, n - 1, bj)
    sol.pop()
    return sol




runtests( iamlate )
