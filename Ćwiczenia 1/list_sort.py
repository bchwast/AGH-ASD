class Node:
    def __init__(self):
        self.next = None
        self.value = None


def printList(L):
    while L != None:
        print(L.value, end = " -> ")
        L = L.next
    print()


def insertNode(node, L):
    start = L
    while L.next != None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node
    return start


def sortList(L):
    head = Node()

    while L.next != None:
        m = L.next
        m_prev = L

        prev = L

        while prev.next != None:
            if prev.next.value > m.value:
                m_prev = prev
                m = prev.next
            prev = prev.next

        m_prev.next = m.next
        head = insertNode(m, head)

    return head


"""L = Node()
nnode = Node()
nnode.value = 2
L.next = nnode
nn = Node()
nn.value = 5
nnode.next = nn
printList(L)
a = Node()
a.value = 1
insertNode(a, L)
printList(L)
b = Node()
b.value = 3
insertNode(b, L)
printList(L)
c = Node()
c.value = 7
insertNode(c, L)
printList(L)"""

L = Node()
a = Node()
b = Node()
c = Node()
d = Node()
a.value = 5
b.value = 1
c.value = 13
d.value = 3
L.next = a
a.next = b
b.next = c
c.next = d
printList(L)
L = sortList(L)
printList(L)