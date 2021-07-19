from math import log2, ceil


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


def binary_search(T, wanted, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if T[mid][0] == wanted:
        return mid
    elif wanted < T[mid][0]:
        return  binary_search(T, wanted, low, mid - 1)
    else:
        return binary_search(T, wanted, mid + 1, high)


def sort_logn_diff(T):
    n = len(T)
    different = [[None, 0] for _ in range(ceil(log2(n)))]

    ind = -1
    for i in range(n):
        key = binary_search(different, T[i], 0, ind)
        if key == None:
            ind += 1
            different[ind][0] = T[ind]
            different[ind][1] = 1
            quicksort(different, 0, ind)
        else:
            different[key][1] += 1

    ind = 0
    for i in range(len(different)):
        for _ in range(different[i][1]):
            T[ind] = different[i][0]
            ind += 1


T = [5, 4, 6, 6, 4, 4, 6, 5]
sort_logn_diff(T)
print(T)