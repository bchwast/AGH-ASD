def partition(T, a, b):
    pivot = T[a]
    i = a - 1
    j = b + 1

    while True:
        i += 1
        while T[i] < pivot:
            i += 1

        j -= 1
        while T[j] > pivot:
            j -= 1

        if i >= j:
            return j

        T[i], T[j] = T[j], T[i]


def quicksort(T, a, b):
    if a < b:
        c = partition(T, a, b)

        quicksort(T, a, c)
        quicksort(T, c + 1, b)


T = [46, 3, 7, 3, 7, 364, -325, -45, -634, 53, 23, 65 ,3]
print(T)
quicksort(T, 0, len(T) - 1)
print(T)