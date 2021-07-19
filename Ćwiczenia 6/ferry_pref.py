"""Dana jest tablica A[n] z długosciami samochodów, które stoja w kolejce,
zeby wjechac na prom. Prom ma dwa pasy (lewy i prawy), oba długosci L. Prosze napisac program, który
wyznacza, które samochody powinny pojechac na który pas, zeby na promie zmiesciło sie jak najwiecej aut.
Auta musza wjezdzac w takiej kolejnosci, w jakiej sa podane w tablicy A."""

# f(i, l) = 1,   pierwsze i samochodów można rozmieścić na promie tak, że zostanie l wolnego miejsca na lewym pasie
#         = 0,   w p. p.

# f(i, l) = {f(i - 1, l + A[i]) || (f(i - 1, l) && sum{(j = 1, i) A[j]} - l <= L}


def fer(A, F, S, L, i, l):
    if l > L or S[i] - l > L:
        return False

    if i < 0:
        return True

    if F[i][l] != None:
        return F[i][l]

    F[i][l] = fer(A, F, S, L, i - 1, l + A[i - 1]) or (fer(A, F, S, L, i - 1, l) and S[i] - l <= L)
    return F[i][l]


def ferry(A, L):
    n = len(A)
    S = [0] * (n + 1)
    F = [[None] * (L + 1) for _ in range(n + 1)]
    # F[i][l]

    F[0][L] = True

    for i in range(n):
        S[i + 1] = S[i] + A[i]

    res = 0
    for i in range(1, n + 1):
        for l in range(L + 1):
            F[i][l] = fer(A, F, S, L, i, l)
            if F[i][l]:
                res = max(res, i)

    return res


A = [1, 2, 3]
L = 3
print(ferry(A, L))