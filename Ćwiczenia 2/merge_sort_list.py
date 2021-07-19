class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def printList(L):
    while L != None:
        print(L.value, end=" -> ")
        L = L.next
    print()


def mergeList(L1, L2):
    head = Node()
    L1 = L1.next
    L2 = L2.next
    tail = head

    while True:
        if L1 is None:
            tail.next = L2
            break

        if L2 is None:
            tail.next = L1
            break

        if L1.value <= L2.value:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    return head


def middleList(L):
    if L.next is None:
        return L

    L = L.next
    slow = L
    fast = L

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeSort(L):
    if L.next is None or L.next.next is None:
        return L

    middle = middleList(L)
    nmiddle = middle.next
    middle.next = None
    R = Node()
    R.next = nmiddle

    L = mergeSort(L)
    R = mergeSort(R)

    F = mergeList(L, R)
    return F


L = Node()
a = Node(5)
b = Node(2)
c = Node(13)
d = Node(35)
e = Node(14)
f = Node(1)
g = Node(48)
L.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

printList(L)
L = mergeSort(L)
printList(L)