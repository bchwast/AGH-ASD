class Node:
    def __init__(self):
        self.next = None
        self.value = None


print("Witaj okrutny świecie!")


def selectionSort(T):
    n = len(T)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if T[minIndex] > T[j]:
                minIndex = j
        T[minIndex], T[i] = T[i], T[minIndex]
    return T


T = [5, 4, 3, 7, 2, 1]
print(selectionSort(T))


def insert_to_node(node, L):
    start = L
    while L.next != None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node
    return start


def printList(L):
    if L is not None:
        print(L.value, end=" ")
        printList(L.next)
    else:
        print()


L = Node()
nnode = Node()
nnode.value = 2
L.next = nnode
nn = Node()
nn.value = 5
nnode.next = nn
printList(L)
a = Node()
a.value = 1
insert_to_node(a, L)
printList(L)
b = Node()
b.value = 3
insert_to_node(b, L)
printList(L)
c = Node()
c.value = 7
insert_to_node(c, L)
printList(L)


def delMax(L):
    m = L.next
    m_prev = L

    prev = L
    L = L.next

    while prev.next != None:
        if prev.next.value > m.value:
            m_prev = prev
            m = prev.next
        prev = prev.next

    m_prev.next = m.next
    return L


# for i in range(5):
#  delMax(L)
#  printList(L)

def binarySearch(T, i, j, x):
    if (i > j):
        return None
    c = (i + j) // 2
    if (T[c] == x):
        retval = binarySearch(T, i, c - 1, x)
        if (retval == None): return c
        return retval
    if (T[c] > x):
        return binarySearch(T, i, c - 1, x)
    else:
        return binarySearch(T, c + 1, j, x)


T1 = [0, 1, 2, 3, 4, 5, 5, 5, 6]
for i in range(len(T1)):
    print(i, binarySearch(T1, 0, len(T1) - 1, T1[i]))

p_inf = 1000
n_inf = -1000


def minmax(T):
    length = len(T)
    minimal = T[length - 1]
    maximal = T[length - 1]
    for i in range(0, length - 1, 2):
        print(i)
        if (T[i] < T[i + 1]):
            T[i], T[i + 1] = T[i + 1], T[i]
        if (T[i] > maximal):
            maximal = T[i]
        if (T[i + 1] < minimal):
            minimal = T[i + 1]
    return maximal, minimal


T = [34, 700, 2, 344, 100, 124, 1000]

print(minmax(T))


def reverse_list(L):
    if L is None:
        return None
    first = L
    p = first.next
    while first is not None:
        p = first
        first = p
        if p is not None:
            p = p.next


def reverse2(L):
    if L is None:
        return

    prev = None

    nxt = L.next

    while L:
        L.next = prev
        prev = L
        L = nxt
        if nxt != None:
            nxt = nxt.next

    return prev


printList(L)
R = reverse2(L)
printList(R)