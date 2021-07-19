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


L1 = Node()
L2 = Node()
a = Node(5)
b = Node(10)
c = Node(15)
d = Node(2)
e = Node(4)
f = Node(9)
L1.next = a
a.next = b
b.next = c
L2.next = d
d.next = e
e.next = f

printList(L1)
printList(L2)
L = mergeList(L1, L2)
printList(L)