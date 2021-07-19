# f(i) - minimalny koszt dotarcia do punktu i

# f(i) = False ; nie da się dotrzeć do i
# f(i + k) = min(F(i) + R(i)) ; i < i + k <= L - S(i + k) - S(i)

def tank(S, P, L, t):
    n = len(S) + 2
    stations = [[None, None] for _ in range(n)]
    stations[0][0], stations[0][1] = 0, 0
    F = [[float("inf"), 0] for _ in range(n)]
    F[0][0], F[0][1] = 0, 0

    for i in range(1, n - 1):
        stations[i][0], stations[i][1] = S[i - 1], P[i - 1]
        if stations[i][0] <= L:
            F[i][0], F[i][1] = 0, 0
    stations[n - 1][0], stations[n - 1][1] = t, 0
    if stations[n - 1][0] <= L:
        F[n - 1][0], F[n - 1][1] = 0, 0

    for i in range(1, n - 1):
        cost = F[i][0] + ((stations[i][0] - stations[F[i][1]][0]) * stations[i][1])
        for k in range(i + 1, n):
            if stations[k][0] - stations[i][0] > L:
                break
            else:
                if F[k][0] > cost:
                    F[k][0], F[k][1] = cost, i

    return F[n - 1][0]


L = 10
S = [8, 11, 15, 16]
P = [40, 7, 15, 12]
t = 23


print(tank(S, P, L, t))