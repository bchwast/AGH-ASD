# f(i, l, r) = 1,   pierwsze i samochodów można rozmieścić na promie tak, że zostanie l wolnego miejsca na lewym pasie
#                   i r wolnego na prawym pasie
#            = 0,   w p. p.

# f(i, l, r) = {f(i - 1, l + A[i], r) || f(i - 1, l, r + A[i])}


def fer(A, F, L, i, l, r):
    if l > L or r > L:
        return False

    if i < 0:
        return True

    if F[i][l][r] != None:
        return F[i][l][r]

    F[i][l][r] = fer(A, F, L, i - 1, l + A[i - 1], r) or fer(A, F, L, i - 1, l, r + A[i - 1])
    return F[i][l][r]


def ferry(A, L):
    n = len(A)
    F = [[[None] * (L + 1) for _ in range(L + 1)] for _ in range(n + 1)]
    # F[i][l][r]

    F[0][L][L] = True

    res = 0
    for i in range(1, n + 1):
        for l in range(L + 1):
            for r in range(L + 1):
                F[i][l][r] = fer(A, F, L, i, l, r)
                if F[i][l][r]:
                    res = max(res, i)

    return res


A = [1, 2, 3]
L = 3
print(ferry(A, L))