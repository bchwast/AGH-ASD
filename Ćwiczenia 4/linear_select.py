import timeit
from random import randint, shuffle


def partition(T, a, b, pivotInd):
    pivot = T[pivotInd]
    T[pivotInd], T[b] = T[b], T[pivotInd]
    i = a - 1
    for j in range(a, b):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[b] = T[b], T[i + 1]
    return i + 1


def ceiling(num):
    copy = int(num // 1)
    if copy == num:
        return copy
    else:
        return copy + 1


def get_median(T, a, b):
    for i in range(a + 1, b + 1):
        el = T[i]
        j = i - 1
        while j >= a and T[j] > el:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = el
    return (a + b) // 2


def magic_fives(T, a, b):
    if b - a < 5:
        return get_median(T, a, b)

    parts = ceiling((b - a + 1) / 5)

    for i in range(parts):
        med = get_median(T, a + (5 * i), min(a + (5 * i) + 4, b))
        T[med], T[a + i] = T[a + i], T[med]

    new_b = a + parts - 1
    return select(T, a, new_b, (a + new_b) // 2)


def select(T, a, b, k):
    if a == b:
        return a
    pivotInd = magic_fives(T, a, b)
    c = partition(T, a, b, pivotInd)
    if c == k:
        return c
    elif k < c:
        return select(T, a, c - 1, k)
    else:
        return select(T, c + 1, b, k)


def linear_select(T, k):
    return T[select(T, 0, len(T) - 1, k)]


n = 1000000
T = [i for i in range(n)]
shuffle(T)
start = timeit.default_timer()
print(linear_select(T, len(T) // 2))
stop = timeit.default_timer()
print(stop - start)
print(sorted(T)[len(T) // 2])
