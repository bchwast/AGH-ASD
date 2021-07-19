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


def sortStrings(T):
    maxL = 0
    for i in range(len(T)):
        if len(T[i]) > maxL:
            maxL = len(T[i])

    buckets = [[] for _ in range(maxL)]

    for i in range(len(T)):
        buckets[len(T[i]) - 1].append(T[i])


    charPos = maxL - 1
    while charPos >= 0:
        countsort(buckets[charPos], 129, charPos)
        if charPos > 0:
            buckets[charPos - 1].extend(buckets[charPos])
            buckets.pop(charPos)
        charPos -= 1

    for i in range(len(T)):
        T[i] = buckets[0][i]


T = ["rudnicki", "duch", "chwast", "matysek", "gozdzielski", "szanca", "scigaj"]
print(T)
sortStrings(T)
print(T)