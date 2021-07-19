def countsort(T, pos):
    occurences = [0] * 26
    result = [None] * len(T)

    for i in range(len(T)):
        occurences[ord(T[i][pos]) - 97] += 1

    for i in range(1, 26):
        occurences[i] += occurences[i - 1]

    for i in range(len(T) - 1, -1, -1):
        occurences[ord(T[i][pos]) - 97] -= 1
        result[occurences[ord(T[i][pos]) - 97]] = T[i]

    for i in range(len(T)):
        T[i] = result[i]


def sortString(A):
    maxL = 0
    for i in range(len(A)):
        if len(A[i]) > maxL:
            maxL = len(A[i])

    buckets = [[] for _ in range(maxL)]

    for i in range(len(A)):
        buckets[len(A[i]) - 1].append(A[i])

    charPos = maxL - 1
    while charPos >= 0:
        countsort(buckets[charPos], charPos)
        if charPos > 0:
            buckets[charPos - 1].extend(buckets[charPos])
            buckets.pop(charPos)
        charPos -= 1

    for i in range(len(A)):
        A[i] = buckets[0][i]


T = ["rudnicki", "duch", "chwast", "matysek", "gozdzielski", "szanca", "scigaj"]
print(T)
sortString(T)
print(T)