from k1_ex2_testy import runtests


class Node:
  def __init__(self):
    self.val = None
    self.next = None 


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


def SortH(p, k):
    Q = []
    head = Node()
    head.val = "|"
    tail = head
    i = 0
    while i <= k and p is not None:
        temp = p
        p = p.next
        temp.next = None
        Q.append((temp.val, temp))
        i += 1

    buildMinHeap(Q)
    while p is not None:
        tail.next = extractMin(Q)[1]
        tail = tail.next
        temp = p
        p = p.next
        temp.next = None
        minHeapInsert(Q, (temp.val, temp))

    while len(Q) > 0:
        tail.next = extractMin(Q)[1]
        tail = tail.next

    return head.next



runtests( SortH )
