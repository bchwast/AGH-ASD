from random import randint


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            quicksort(A, p, q - 1)
            p = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q - 1


def insert(T, key, n):
    T[n] = key
    i = n
    while i > 0 and T[i] > T[parent(i)]:
        T[i], T[parent(i)] = T[parent(i)], T[i]
        i = parent(i)


def iterative_quicksort(T):
    S = []
    p = 0
    r = len(T) - 1
    S.append((p, r))
    while len(S) > 0:
        (p, r) = S.pop()
        if p < r:
            q = partition(T, p, r)
            if q - p > r - q:
                S.append((p, q - 1))
                S.append((q + 1, r))
            else:
                S.append((q + 1, r))
                S.append((p, q - 1))


def lider(T):
    cnt = 1
    l = T[0]
    for i in range(1, len(T)):
        if l == T[i]:
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                l = T[i]
                cnt = 1
    cnt = 0
    for i in range(len(T)):
        if T[i] == l:
            cnt += 1

    if cnt > len(T) // 2:
        return l
    return None


x = lider([2, 3, 2, 4, 5, 2, 2, 1, 5, 2])
print(x)


def hoare(A, p, r):
    x = A[p]
    i = p
    j = r
    while i < r and j > p:
        while A[j] >= x and j > p:
            j -= 1
        while A[i] <= x and i < r:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j


def qsort(A, p, r):
    if p < r:
        q = hoare(A, p, r)
        qsort(A, p, q - 1)
        qsort(A, q + 1, r)


T = [3, 1, 6, 2, 3]

print(T)
qsort(T, 0, len(T) - 1)
print(T)