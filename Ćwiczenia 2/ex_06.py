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
        med = partition(T, low, high)
        if med - low < high - med:
            quicksort(T, low, med - 1)
            low = med + 1
        else:
            quicksort(T, med + 1, high)
            high = med - 1


def scopes(T):
    edges = [[0, 0, '', 0] for _ in range(2 * len(T))]    # współrzędna, indeks, pocz/kon, il. pocz/kon. wczes/row
    for i in range(len(T)):
        edges[2 * i] = [T[i][0], i, 'b', 0]
        edges[(2 * i) + 1] = [T[i][1], i, 'e', 0]

    quicksort(edges, 0, len(edges) - 1)

    amm_b, amm_e = 0, 0
    last_b, last_e = -1, -1
    for i in range(len(edges)):
        if edges[i][2] == 'b':
            if edges[i][0] != last_b:
                amm_b += 1
                last_b = edges[i][0]
            edges[i][3] = amm_b
        else:
            if edges[i][0] != last_e:
                amm_e += 1
                last_e = edges[i][0]
            edges[i][3] = amm_e

    ranges = [[T[i][0], T[i][1], 0, 0] for i in range(len(T))]
    for i in range(len(edges)):
        if edges[i][2] == 'b':
            ranges[edges[i][1]][0], ranges[edges[i][1]][2] = edges[i][0], edges[i][3]
        else:
            ranges[edges[i][1]][1], ranges[edges[i][1]][3] = edges[i][0], edges[i][3]

    max_r, ind = -1, 0
    for i in range(len(T)):
        if ranges[i][3] - ranges[i][2] > max_r:
            max_r = ranges[i][3] - ranges[i][2]
            ind = i

    return ind



T = [(4, 5), (0, 12), (0, 3), (0, 14), (2, 6), (2, 19), (1, 19)]
print(scopes(T))