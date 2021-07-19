def partition(T, a, b):
    pivot = T[b]
    i = a - 1
    for j in range(a, b):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[b] = T[b], T[i + 1]
    return i + 1


def quicksort(T, a, b):
    if a < b:
        c = partition(T, a, b)
        quicksort(T, a, c - 1)
        quicksort(T, c + 1, b)


T = [5, 6, 23, 6, 23, 6, 345]
quicksort(T, 0, len(T) - 1)
print(T)
