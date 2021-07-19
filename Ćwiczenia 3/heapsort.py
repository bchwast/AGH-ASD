def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


def heapify(T, n, i):
    m = i
    if left(i) < n and T[left(i)] > T[m]:
        m = left(i)
    if right(i) < n and T[right(i)] > T[m]:
        m = right(i)

    if m != i:
        T[m], T[i] = T[i], T[m]
        heapify(T, n, m)


def buildHeap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def heapsort(T):
    n = len(T)
    buildHeap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)


T = [35, 632, 327, -324, 3, 478, 3, 4576, 34576234675, 3, 46763, 26, 7, -234, 7, 15, -5, 33, -46, -36, -46, -6,
     -363 - 36, 34]

heapsort(T)
print(T)
