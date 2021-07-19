def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


def maxHeapify(T, n, i):
    m = i
    if left(i) < n and T[left(i)] > T[m]:
        m = left(i)
    if right(i) < n and T[right(i)] > T[m]:
        m = right(i)

    if m != i:
        T[m], T[i] = T[i], T[m]
        maxHeapify(T, n, m)


def buildMaxHeap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        maxHeapify(T, n, i)


def maxHeapInsert(T, el):
    T.append(el)
    curr = len(T) - 1
    while curr > 0 and T[curr] > T[parent(curr)]:
        T[curr], T[parent(curr)] = T[parent(curr)], T[curr]
        curr = parent(curr)


def extractMax(T):
    el = T[0]
    T[0], T[len(T) - 1] = T[len(T) - 1], T[0]
    T.pop(len(T) - 1)
    maxHeapify(T, len(T), 0)
    return el


T = [1, 2, 3, 4, 5, 6, 7, 8]
buildMaxHeap(T)
print(T)
maxHeapInsert(T, 10)
print(T)
print(extractMax(T))
print(T)

