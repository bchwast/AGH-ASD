import timeit
from random import randint

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def tab2list(T):
    head = Node()
    tail = head
    for i in range(len(T)):
        el = Node()
        el.value = T[i]
        tail.next = el
        tail = el
    return head.next


def printList(L):
    while L != None:
        print(L.value, end=" -> ")
        L = L.next
    print("|")


def getTail(L):
    if L == None or L.next == None:
        return L

    prev = None
    while L != None:
        prev = L
        L = L.next

    return prev


def partition(L, pivot):
    smaller = Node()
    tail_s = smaller
    equal = Node()
    tail_e = equal
    larger = Node()
    tail_l = larger

    while L != None:
        if L.value < pivot.value:
            tail_s.next = L
            tail_s = tail_s.next
        elif L.value == pivot.value:
            tail_e.next = L
            tail_e = tail_e.next
        else:
            tail_l.next = L
            tail_l = tail_l.next
        L = L.next

        tail_s.next = None
        tail_e.next = None
        tail_l.next = None

    return smaller, tail_s, equal.next, tail_e, larger, tail_l


def quicksort(Head, Tail):
    if Head == Tail:
        return Head, Tail

    sHead, sTail, eHead, eTail, lHead, lTail = partition(Head, Head)

    if sHead == sTail:
        sHead = eHead
        sTail = eHead
    else:
        sHead = sHead.next
        sHead, sTail = quicksort(sHead, sTail)
        sTail.next = eHead

    if lHead == lTail:
        lHead = eTail
        lTail = eTail
    else:
        lHead = lHead.next
        lHead, lTail = quicksort(lHead, lTail)
        eTail.next = lHead

    return sHead, lTail


def qsort(L):
    if L == None:
        return None

    l = getTail(L)
    L, _ = quicksort(L, l)
    return L



T = [randint(-1000,1000) for _ in range(100000)]
L = tab2list(T)


start = timeit.default_timer()
L = qsort(L)
stop = timeit.default_timer()
print(stop - start)
