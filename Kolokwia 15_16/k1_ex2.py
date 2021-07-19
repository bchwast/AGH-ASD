from math import log2, ceil

def partition(T, low, high):
    pivot = T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[high] = T[high], T[i + 1]
    return i + 1


def quicksort(T, low, high):
    while low < high:
        med = partition(T, low, high)
        if med - low < high - med:
            quicksort(T, low, med - 1)
            low = med + 1
        else:
            quicksort(T, med + 1, high)
            high = med - 1


def repair_sort(A):
    result = [None] * len(A)
    evens = [None] * ceil(log2(len(A)))

    ind = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            evens[ind] = A[i]
            ind += 1
            A[i] = 0

    quicksort(evens, 0, len(evens) - 1)

    ind_A, ind_e, ind_r = 0, 0, 0
    while ind_r < len(A) and ind_A < len(A) and ind_e < len(evens):
        if A[ind_A] == 0:
            ind_A += 1
        elif A[ind_A] < evens[ind_e]:
            result[ind_r] = A[ind_A]
            ind_r += 1
            ind_A += 1
        else:
            result[ind_r] = evens[ind_e]
            ind_r += 1
            ind_e += 1

    while ind_A < len(A):
        if A[ind_A] != 0:
            result[ind_r] = A[ind_A]
            ind_r += 1
        ind_A += 1
    while ind_e < len(evens):
        result[ind_r] = evens[ind_e]
        ind_r += 1
        ind_e += 1

    for i in range(len(A)):
        A[i] = result[i]


T = [1, 3, 6, 7, 4, 11, 4, 15]
repair_sort(T)
print(T)