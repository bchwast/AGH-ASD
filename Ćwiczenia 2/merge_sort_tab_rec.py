def merge(L, R):
    F = [0]*(len(L) + len(R))

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            F[k] = L[i]
            i += 1
        else:
            F[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        F[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        F[k] = R[j]
        j += 1
        k += 1

    return F


def mergeSort(T):
    if len(T) > 1:
        c = (len(T))//2

        L = T[:c]
        R = T[c:]

        L = mergeSort(L)
        R = mergeSort(R)

        return merge(L, R)
    else:
        return T


T = [4, 6, 324, 54, 3, 6, 23, 64, 235 ,7]
print(T)
T = mergeSort(T)
print(T)