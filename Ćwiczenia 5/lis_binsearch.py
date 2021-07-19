def get_index(T, tails, low, high, value):
    if 1 < high - low:
        mid = (low + high) // 2
        if T[tails[mid]] == value:
            return mid
        elif T[tails[mid]] > value:
            return get_index(T, tails, low, mid, value)
        else:
            return get_index(T, tails, mid , high, value)
    return high


def get_solution(T, parent, ind):
    if parent[ind] == -1:
        return [T[ind]]
    return get_solution(T, parent, parent[ind]) + [T[ind]]


def lis(T):
    tails = [0] * len(T)
    parent = [-1] * len(T)
    length = 1

    for i in range(len(T)):
        if T[i] < T[tails[0]]:
            tails[0] = i
        elif T[tails[length - 1]] < T[i]:
            tails[length] = i
            parent[i] = tails[length - 1]
            length += 1
        else:
            pos = get_index(T, tails, 0, length - 1, T[i])
            tails[pos] = i
            parent[i] = tails[pos - 1]

    result = get_solution(T, parent, tails[length - 1])
    return length, result


T = [13, 7, 21, 42, 8, 2, 44, 53]
print(lis(T))
