# 2 pkt

from e1_ex1_testy import runtests
from queue import PriorityQueue


def chaos_index( T ):
    n = len(T)
    Q = PriorityQueue()

    for i in range(n):
        Q.put([T[i], i])

    k = 0
    for i in range(n):
        tmp = Q.get()
        k = max(k, abs(tmp[1] - i))

    return k


runtests( chaos_index )
