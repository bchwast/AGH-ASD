from random import randint


def partition(T, low, high):
    pivot = T[high][0]
    i = low - 1
    for j in range(low, high):
        if T[j][0] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[high] = T[high], T[i + 1]
    return i + 1


def quicksort(T, low, high):
    while low < high:
        mid = partition(T, low, high)
        if mid - low < high - mid:
            quicksort(T, low, mid - 1)
            low = mid + 1
        else:
            quicksort(T, mid + 1, high)
            high = mid - 1


def SumSort(A, B, n):
    sums = [[0, i] for i in range(n)]

    for i in range(n):
        for j in range(i * n, (i + 1) * n):
            sums[i][0] += A[j]

    quicksort(sums, 0, n - 1)

    ind = 0
    for i in range(n):
        mult = sums[i][1]
        for j in range(mult * n, (mult + 1) * n):
            B[ind] = A[j]
            ind += 1


n = 10
A = [randint(-1000, 1000) for _ in range(n * n)]
B = [0] * (n * n)
SumSort(A, B, n)
print(B)
sums = 0
for i in range(n * n):
    if i % n == 0:
        print(sums)
        sums = 0
    sums += B[i]
