from random import randint


class Node:
    def __init__(self):
        self.value = None
        self.next = None


class TwoLists:
    def __init__(self):
        self.even = None
        self.odd = None


def tab2list(T):
    head = Node()
    tail = head
    for i in range(len(T)):
        el = Node()
        el.value = T[i]
        tail.next = el
        tail = el
    return head.next


def print_list(L):
    while L != None:
        print(L.value, end=" -> ")
        L = L.next
    print("|")


def split(list):
    even_h = Node()
    odd_h = Node()
    even_t = even_h
    odd_t = odd_h

    while list != None:
        if list.value % 2 == 0:
            even_t.next = list
            even_t = list
        else:
            odd_t.next = list
            odd_t = list
        list = list.next

    even_t.next = None
    odd_t.next = None

    head = TwoLists()
    head.even = even_h.next
    head.odd = odd_h.next

    return head


T = [randint(-1000, 1000) for _ in range(20)]
L = tab2list(T)
print_list(L)
res = split(L)
print_list(res.odd)
print_list(res.even)