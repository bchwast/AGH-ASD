"""Dane: n przedmiotów, W[i] - waga i-tego przedmiotu, P[i] - zysk z i-tego przedmiotu, MaxW - maksymalna dopuszczalna
         wwaga plecaka
   Zadanie: Wybrać przedmioty o jak największym sumarycznym zysku, nie przekraczające łącznie wagi MaxW"""

# f(i, w) - maksymalny zysk z wzięcia przedmiotów od 0 do i przy wadze nie przekraczającej w

# f(i, 0) = 0
# f(0, w) = 0 ; W[0] > MaxW
# f(0, w) = P[0] ; W[0] <= MaxW
# f(i, w) = max(f(i - 1, w), f(i - 1, w - W[i]) + P[i])) ; w >= W[i]


def knapsack(W, P, MaxW):
    n = len(W)
    F = [[0] * (MaxW + 1) for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])

    return F[n - 1][MaxW], F


def get_solution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]: return [0]
        return []
    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]
    return get_solution(F, W, P, i - 1, w)


P = [21, 3, 6, 3, 87, 34, 7, 34, 97, 34]
W = [4, 5, 12, 9, 1, 13, 2, 5, 2, 5]
MaxW = 30

res, F = knapsack(W, P, MaxW)
solution = get_solution(F, W, P, len(P) - 1, MaxW)
print(res)