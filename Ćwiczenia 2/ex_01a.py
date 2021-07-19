def merge(T, a, c, b):
    n1 = c - a + 1
    n2 = b - c
    L = [0]*n1
    R = [0]*n2
    for i in range(n1):
        L[i] = T[a + i]
    for i in range(n2):
        R[i] = T[c + i + 1]

    i = j = 0
    k = a
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        T[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        T[k] = R[j]
        j += 1
        k += 1

    return T


def nat(T, a):
    n = len(T)
    i = a + 1
    prev = T[a]
    while i < len(T) and prev <= T[i]:
        prev = T[i]
        i += 1

    return a, i - 1


def mergeSort(T):
    if T == []:
        return T
    while True:
        a, c, b = 0, 0, 0
        while a <= len(T) - 1:
            a, c = nat(T, a)
            if a == 0 and c == len(T)-1:
                return T

            if c == len(T) - 1:
                break

            _, b = nat(T, c + 1)
            T = merge(T, a, c, b)

            a = b + 1


T = [1,2,4,3]
print(T)
T = mergeSort(T)
print(T)