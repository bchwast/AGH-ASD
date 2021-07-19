"""Pewna zaba skacze po osi liczbowej. Ma sie dostac z zera do n − 1, skaczac
wyłacznie w kierunku wiekszych liczb. Skok z liczby i do liczby j (j > i) kosztuje ja j − i jednostek energii, a
jej energia nigdy nie moze spasc ponizej zera. Na poczatku zaba ma 0 jednostek energii, ale na szczescie na
niektórych liczbach—takze na zerze—leza przekaski o okreslonej wartosci energetycznej (wartosc przekaki
dodaje sie do aktualnej energii Zbigniewa). Prosze zaproponowac algorytm, który oblicza minimalna liczbe
skoków potrzebna na dotarcie z 0 do n − 1 majac dana tablice A z wartosciami energetycznymi przekasek na
kazdej z liczb."""

# f(i, e) - minimalna ilość skoków, które Zbigniew musi wykonać, żeby dostać się od 0 do i posiadając e energii

# f(0, j) = 0 ; 0 <= j <= A[0]
# f(i, e) = min(f(k, e + (i - k) - A[i])) ; 0 <= k < i
# f(i, -e) = inf

# f(i + k, e - k + A[i + k]) = min(f(i + k, e - k + A[i + k]), f(i, e) + 1) ; 0 <= k < e
# f(0, j) = 0 ; 0 <= j <= A[0]
# w p. p. - f(i, e) = inf


def zbycholud(A, F, i, e):
    if F[i][e] != float("inf"):
        return F[i][e]

    res = float("inf")
    for k in range(i):
        if 0 <= e + i - k - A[i] < len(F[k]):
            res = min(res, zbycholud(A, F, k, e + i - k - A[i]))
    F[i][e] = res + 1
    return F[i][e]


def zbigniew(A):
    n = len(A)
    F = [[float("inf")] * (n + 1) for _ in range(n)]
    for e in range(A[0] + 1):
        F[0][e] = 0

    res = float("inf")
    for e in range(n):
        zbycholud(A, F, n - 1, e)
        res = min(res, F[n - 1][e])

    return res


# def zbigniew(A):
#     n = len(A)
#
#     F = [[float("inf")] * (n + 1) for _ in range(n)]
#     for e in range(A[0] + 1):
#         F[0][e] = 0
#
#     for i in range(n):
#         for e in range(1, n + 1):
#             if F[i][e] != float("inf"):
#                 for k in range(e):
#                     if i + k < n and e - k + A[i + k] <= n:
#                         F[i + k][e - k + A[i + k]] = min(F[i + k][e - k + A[i + k]], F[i][e] + 1)
#
#     res = float("inf")
#     for e in range(n + 1):
#         res = min(res, F[n-1][e])
#
#     return res


A = [4, 5, 2, 4, 1, 2, 1, 0]
print(zbigniew(A))