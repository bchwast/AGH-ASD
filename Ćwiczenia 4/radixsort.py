def countsort(T, k, pos):
    occurences = [0] * k
    result = [0] * len(T)

    for i in range(len(T)):
        occurences[ord(T[i][pos])] += 1

    for i in range(1, k):
        occurences[i] += occurences[i - 1]

    for i in range(len(T) - 1, -1, -1):
        occurences[ord(T[i][pos])] -= 1
        result[occurences[ord(T[i][pos])]] = T[i]

    for i in range(len(T)):
        T[i] = result[i]


def radixsort(T):
    charPos = len(str(max(T))) - 1

    while charPos >= 0:
        countsort(T, 129, charPos)
        charPos -= 1


T = ["kra", "art", "kot", "kit", "ati", "kil"]
radixsort(T)
print(T)