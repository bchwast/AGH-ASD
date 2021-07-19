from kp2_ex1_testy import runtests

def partition(T, low, high):
    pivot = T[high][0][0]
    i = low - 1
    for j in range(low, high):
        if T[j][0][0] >= pivot:
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


def dominance(P):
    S = []
    points = [[P[i], i] for i in range(len(P))]
    quicksort(points, 0, len(P) - 1)

    start = [float("inf"), float("inf")]
    for i in range(len(P) - 1, -1, -1):
        if points[i][0][1] < start[1] or points[i][0] == start:
            start = points[i][0]
            S.append(points[i][1])

    return S


runtests(dominance)

# P = [(2, 2), (1, 1), (2.5, 0.5), (0.5, 0.5), (3, 2), (0.5, 3), (0.5, 0.5)]
# S = dominance(P)
# print(S)