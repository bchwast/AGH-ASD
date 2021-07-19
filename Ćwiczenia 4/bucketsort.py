def insertionsort(T):
    for i in range(1, len(T)):
        el = T[i]
        j = i - 1
        while j >= 0 and T[j] > el:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = el


def bucketsort(T):
    maxEl, minEl = max(T), min(T)
    bucketTab = [[] for _ in range(len(T))]
    bucketRange = (maxEl - minEl) / len(T)
    for i in range(len(T)):
        bucketTab[min(int((T[i] - minEl) / bucketRange), len(T) - 1)].append(T[i])

    for i in range(len(T)):
        insertionsort(bucketTab[i])

    ind = 0
    for i in range(len(T)):
        for j in range(len(bucketTab[i])):
            T[ind] = bucketTab[i][j]
            ind += 1


T = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
bucketsort(T)
print(T)