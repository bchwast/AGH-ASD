def min_max(T):
    n = len(T)
    min_el = T[n - 1]
    max_el = T[n - 1]

    for i in range(0, n - 1, 2):
        if T[i + 1] < T[i]:
            T[i], T[i + 1] = T[i + 1], T[i]
        if T[i] < min_el:
            min_el = T[i]
        if max_el < T[i + 1]:
            max_el = T[i + 1]

    return min_el, max_el


T = [4, 3, 2, 10, 12, 1, 5, 6, -2]
print(min_max(T))