# 2 pkt

from random import randint

def partition(T, low, high, pivotInd):
    pivot = T[pivotInd]
    T[high], T[pivotInd] = T[pivotInd], T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] >= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[high] = T[high], T[i + 1]
    return i + 1


def make_parts(T, low, high, wanted):
    if low == high:
        return
    mid = partition(T, low, high, high)
    if mid == wanted:
        return
    elif wanted < mid:
        return make_parts(T, low, mid - 1, wanted)
    else:
        return make_parts(T, mid + 1, high, wanted)


def quicksort(T, low, high):
    while low < high:
        mid = partition(T, low, high, high)
        if mid - low < high < mid:
            quicksort(T, low, mid - 1)
            low = mid + 1
        else:
            quicksort(T, mid + 1, high)
            high = mid - 1


def section(T, p, q):
    result = [0] * (q - p + 1)
    make_parts(T, 0, len(T) - 1, p)
    make_parts(T, p, len(T) - 1, q)
    quicksort(T, p, q)
    ind = 0
    for i in range(p, q + 1):
        result[ind] = T[i]
        ind += 1
    return result

T = [randint(170, 210) for _ in range(20)]
print(section(T, 5, 12))
print(sorted(T, reverse=True))
