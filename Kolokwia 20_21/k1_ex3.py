# 2 pkt

from k1_ex3_testy import runtests


def insertionsort(T):
    for i in range(1, len(T)):
        el = T[i]
        j = i - 1
        while j >= 0 and T[j] > el:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = el


def bucketsort(T, mode):
    if len(T) <= 1:
        return
    maxEl, minEl = max(T), min(T)
    if maxEl == minEl:
        return
    bucketTab = [[] for _ in range(len(T))]
    bucketRange = (maxEl - minEl) / len(T)
    for i in range(len(T)):
        bucketTab[min(int((T[i] - minEl) / bucketRange), len(T) - 1)].append(T[i])

    if mode == 0:
        for i in range(len(T)):
            bucketsort(bucketTab[i], 1)
    else:
        for i in range(len(T)):
            insertionsort(bucketTab[i])

    ind = 0
    for i in range(len(T)):
        for j in range(len(bucketTab[i])):
            T[ind] = bucketTab[i][j]
            ind += 1


def SortTab(T,P):
    bucketsort(T, 0)
    return

runtests( SortTab )