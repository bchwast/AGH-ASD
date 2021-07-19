def binary_search_repetitions(T, low, high, wanted):
    if low <= high:
        mid = (low + high) // 2
        if T[mid] == wanted:
            key = binary_search_repetitions(T, low, mid - 1, wanted)
            if key is None:
                return mid
            return key
        elif wanted < T[mid]:
            return binary_search_repetitions(T, low, mid - 1, wanted)
        else:
            return binary_search_repetitions(T, mid + 1, high, wanted)
    return