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
    tail = head
    for i in range(len(T)):
        el = Node()
        el.value = T[i]
        tail.next = el
        tail = tail.next
    return head.next


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

    if L1 != None:
        tail.next = L1
    if L2 != None:
        tail.next = L2

    while tail.next != None:
        tail = tail.next

    return head.next, tail


def nat(L):
    A = L
    while A.next != None and A.value <= A.next.value:
        A = A.next

    B = A.next
    A.next = None
    return B, A


def mergeSort(L):
    while True:
        NH = None
        NT = None
        while True:
            if L == None:
                L = NH
                break

            A = L
            L, T = nat(L)

            if NT == None and L == None:
                return A

            if L == None:
                NT.next = A
                L = NH
                break

            B = L
            L, _ = nat(L)

            X, T = merge(A, B)

            if NH == None:
                NH = X
            else:
                NT.next = X
            NT = T


"""def mergeSort(L):
    while True:
        NH = None
        NT = None
        while True:
            A = L
            NH = nat(L)
            NT = nat(NH)

            NH, X = merge(L, NH)
            X.next = NT


def paste(L):
    A = L
    NH = nat(L)
    NT = nat(NH)

    NH, X = merge(L, NH)
    printList(NH)
    X.next = NT
    printList(X)"""


T = [5,3,7,3,7]
L = tab2list(T)
printList(L)
L = mergeSort(L)
printList(L)
#paste(L)
