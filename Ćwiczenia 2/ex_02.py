def merge(T, a, c, b, cnt):
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
            cnt += 1
        k += 1

    while i < n1:
        T[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        T[k] = R[j]
        j += 1
        k += 1

    return T, cnt


def inversions(T, a, b, cnt):
    if a < b:
        c = (a+b)//2
        T, cnt = inversions(T, a, c, cnt)
        T, cnt = inversions(T, c + 1, b, cnt)
        T, cnt = merge(T, a, c, b, cnt)
        return T, cnt
    else:
        return T, cnt


T = [2,1,234,5,5,6]
T, cnt = inversions(T, 0, len(T) - 1, 0)
print(cnt)