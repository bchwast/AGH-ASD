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


def sort_unique(T):
    temp = [T[i] for i in range(len(T))]
    quicksort(temp, 0, len(temp) - 1)

    uniq = [temp[0]]
    for i in range(1, len(temp)):
        if not temp[i] in uniq:
            uniq.append(temp[i])

    return uniq


def lcs(A, B):
    n_A = len(A)
    n_B = len(B)
    F = [[0] * n_A for _ in range(n_B)]

    for i in range(n_A):
        if A[i] == B[0]:
            F[0][i] = 1
    for j in range(n_B):
        if A[0] == B[j]:
            F[j][0] = 1

    for j in range(1, n_B):
        for i in range(1, n_A):
            if A[i] == B[j]:
                F[j][i] = F[j - 1][i - 1] + 1
            else:
                F[j][i] = max(F[j - 1][i], F[j][i - 1])

    return F[n_B - 1][n_A - 1]


def lis(T):
    uniq = sort_unique(T)

    return lcs(T, uniq)


T = [13, 7, 21, 42, 8, 2, 44, 53]
print(lis(T))