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
        k+= 1

    while i < n1:
        T[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        T[k] = R[j]
        j += 1
        k += 1

    return T


def mergeSort(T):
    size = 1

    while size < len(T):
        a = 0
        while a < len(T)-1:
            if (2*size + a - 1) < len(T)-1:
                b = 2*size + a - 1
            else:
                b = len(T) - 1

            c = min(a + size - 1, len(T) - 1)

            T = merge(T, a, c, b)
            a += 2*size

        size *= 2

    return T


T = [1, 43, 3, 1]
print(T)
T = mergeSort(T)
print(T)