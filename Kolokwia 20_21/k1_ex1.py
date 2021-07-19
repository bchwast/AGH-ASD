from k1_ex1_testy import runtests


def partition(T, a, b):
    pivotInd = b
    pivot = T[pivotInd]
    i = a - 1
    for j in range(a, b):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[b] = T[b], T[i + 1]
    return i + 1


def quickselect(T, a, b, k):
    if a == b:
        return T[a]
    c = partition(T, a, b)
    if c == k:
        return T[c]
    elif k < c:
        return quickselect(T, a, c - 1, k)
    else:
        return quickselect(T, c + 1, b, k)


def Median(T):
    n = len(T)
    A = [None] * (n * n)
    ind = 0
    for i in range(n):
        for j in range(n):
            A[ind] = T[i][j]
            ind += 1
    quickselect(A, 0, (n * n) - 1, ((n // 2) * n) - 1)
    quickselect(A, (n // 2) * n, (n * n) - 1, (((n // 2) + 1) * n) - 1)
    ind = 0
    a = 1
    for i in range(n):
        for j in range(a, n):
            T[j][i] = A[ind]
            ind += 1
        a += 1
    for i in range(n):
        T[i][i] = A[ind]
        ind += 1
    a = 1
    for i in range(n):
        for j in range(a, n):
            T[i][j] = A[ind]
            ind += 1
        a += 1


runtests( Median ) 
