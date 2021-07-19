def binary_search(T, low, high, wanted):
    if low <= high:
        mid = (high + low) // 2
        if T[mid] == wanted:
            return mid
        elif wanted < T[mid]:
            return binary_search(T, low, mid - 1, wanted)
        else:
            return binary_search(T, mid + 1, high, wanted)
    else:
        return