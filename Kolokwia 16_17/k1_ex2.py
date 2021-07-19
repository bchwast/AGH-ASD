def partition(T, low, high, pivotInd):
    pivot = T[pivotInd]
    T[pivotInd], T[high] = T[high], T[pivotInd]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[high] = T[high], T[i + 1]
    return i + 1


def make_parts(T, low, high, wanted):
    if low == high:
        return
    mid = partition(T, low, high, wanted)
    if mid == wanted:
        return
    elif wanted < mid:
        return make_parts(T, low, mid - 1, wanted)
    else:
        return make_parts(T, mid + 1, high, wanted)


def SumBetween(T, p, q):
    make_parts(T, 0, len(T) - 1, p)
    make_parts(T, p, len(T) - 1, q)

    result = 0
    for i in range(p, q + 1):
        result += T[i]

    return result


T = [3, 13, 6, 21, 9, 75, 43, 12, 2, 84, 24, 14, 10, 8]
print(SumBetween(T, 7, 12))
print(sorted(T))