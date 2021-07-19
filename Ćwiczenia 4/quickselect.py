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


T = [3, 4, 6, 23, 7, 324, 25, 7,23 ,346, 3,46, 436,3, 2, 57654, 43,34]
print(T)
for i in range(len(T)):
    print(quickselect(T, 0, len(T) - 1, i))
print(sorted(T))