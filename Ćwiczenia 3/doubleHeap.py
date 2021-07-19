def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


def minHeapify(T, n, i):
    m = i
    if left(i) < n and T[left(i)] < T[m]:
        m = left(i)
    if right(i) < n and T[right(i)] < T[m]:
        m = right(i)

    if m != i:
        T[m], T[i] = T[i], T[m]
        minHeapify(T, n, m)


def buildMinHeap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        minHeapify(T, n, i)


def minHeapInsert(T, el):
    T.append(el)
    curr = len(T) - 1
    while curr > 0 and T[curr] < T[parent(curr)]:
        T[curr], T[parent(curr)] = T[parent(curr)], T[curr]
        curr = parent(curr)


def extractMin(T):
    el = T[0]
    T[0], T[len(T) - 1] = T[len(T) - 1], T[0]
    T.pop(len(T) - 1)
    minHeapify(T, len(T), 0)
    return el


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


def Initialize():
    minHeap = []
    maxHeap = []
    T = [minHeap, maxHeap]
    return T


def Insert(T, el):
    if len(T[0]) == 0 or el >= T[0][0]:
        minHeapInsert(T[0], el)
    else:
        maxHeapInsert(T[1], el)

    if len(T[0]) > len(T[1]) + 1:
        maxHeapInsert(T[1], extractMin(T[0]))
    elif len(T[1]) > len(T[0]) + 1:
        minHeapInsert(T[0], extractMax(T[1]))


def GetMedian(T):
    if len(T[0]) > len(T[1]):
        return T[0][0]
    elif len(T[1]) > len(T[0]):
        return T[1][0]
    else:
        return (T[0][0] + T[1][0]) / 2


T = [1,2,3,4]
H = Initialize()
for i in range(len(T)):
    Insert(H, T[i])
print(GetMedian(H))