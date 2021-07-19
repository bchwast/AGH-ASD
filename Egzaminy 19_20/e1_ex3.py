# 2 pkt

from e1_ex3_testy import runtests
from math import log


def insertionsort(T):
    for i in range(1, len(T)):
        el = T[i]
        j = i - 1
        while j >= 0 and T[j] > el:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = el


def fast_sort(tab, a):
    maxEl, minEl = log(max(tab), a), log(min(tab), a)
    bucketTab = [[] for _ in range(len(tab))]
    bucketRange = (maxEl - minEl) / len(tab)
    for i in range(len(tab)):
        bucketTab[min(int((log(tab[i], a) - minEl) / bucketRange), len(tab) - 1)].append(tab[i])

    for i in range(len(tab)):
        insertionsort(bucketTab[i])

    ind = 0
    for i in range(len(tab)):
        for j in range(len(bucketTab[i])):
            tab[ind] = bucketTab[i][j]
            ind += 1

    return tab



runtests( fast_sort )
