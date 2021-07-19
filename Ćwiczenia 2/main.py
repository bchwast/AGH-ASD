class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printList(L):
    while L != None:
        print(L.value, end=" -> ")
        L = L.next
    print("|")


def tab2list(T):
    head = Node()
    for i in range(len(T)):


def merge(L1, L2):
    head = Node()
    tail = head
    while L1 != None and L2 != None:
        if L1.value <= L2.value:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    if L1 != None: tail.next = L2
    if L2 != None: tail.next = L1
    while tail.next != None:
        tail = tail.next

    return head.next, tail


def cutList(L):
    if L == None:
        return None

    while L.next != None and L.next.value >= L.value:
        L = L.next

    H = L.next
    L.next = None
    return H


def mergeSort(L):
    if L == None:
        return None

    tail = cutList(L)
    S = L
    L = tail
    while L != None:
        tail = cutList(L)
        S = merge(S, L)
        L = tail

    return S


