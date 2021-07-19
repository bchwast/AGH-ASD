def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


def minHeapify(T, n, i):
    m = i
    if left(i) < n and T[left(i)][0] < T[m][0]:
        m = left(i)
    if right(i) < n and T[right(i)][0] < T[m][0]:
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
    while curr > 0 and T[curr][0] < T[parent(curr)][0]:
        T[curr], T[parent(curr)] = T[parent(curr)], T[curr]
        curr = parent(curr)


def extractMin(T):
    el = T[0]
    T[0], T[len(T) - 1] = T[len(T) - 1], T[0]
    T.pop(len(T) - 1)
    minHeapify(T, len(T), 0)
    return el


def sortTabs(Tabs):
    k = len(Tabs)
    n = 0

    heap = [None]*k
    for i in range(k):
        n += len(Tabs[i])
        heap[i] = [Tabs[i][0], i]
    T = [None]*n

    pointers = [[i, 0] for i in range(k)]

    for i in range(n):
        T[i], p = extractMin(heap)
        pointers[p][1] += 1
        if pointers[p][1] < len(Tabs[p]):
            minHeapInsert(heap, [Tabs[p][pointers[p][1]], p])

    return T


Tabs = [[1,2,3,4],[3,5,6],[1,2,2,2,2,2,]]
T = sortTabs(Tabs)
print(T)



