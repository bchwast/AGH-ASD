def countsort(T, pos):
    occurences = [0] * 2
    result = [None] * len(T)

    for i in range(len(T)):
        occurences[ord(T[i][pos]) - 97] += 1

    occurences[1] += occurences[0]

    for i in range(len(T) - 1, -1, -1):
        occurences[ord(T[i][pos]) - 97] -= 1
        result[occurences[ord(T[i][pos]) - 97]] = T[i]

    for i in range(len(T)):
        T[i] = result[i]


def repeats(sequence, k):
    n = len(sequence)
    T = [None] * (n - k + 1)
    for i in range(n - k + 1):
        T[i] = sequence[i:i + k:]

    for i in range(k - 1, -1, -1):
        countsort(T, i)

    cnt, max_cnt, ind, curr = 1, 1, 0, 1
    while curr < n - k + 1:
        if T[curr] == T[curr - 1]:
            cnt += 1
        else:
            cnt = 1

        if cnt > max_cnt:
            max_cnt = cnt
            ind = curr

        curr += 1

    return T[ind]





print(repeats("ababaaabb", 3))