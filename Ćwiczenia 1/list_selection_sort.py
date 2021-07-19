class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def wypisz(first):
    if first is None:
        return
    p = first
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print()


def swap(first, el1, el2, prev_el2):
    first = el2
    prev_el2.next = el1

    el1.next, el2.next = el2.next, el1.next
    return first


def selection_sort(first):
    if first is None or first.next is None:
        return first

    min = first
    befmin = None
    p = first

    while p.next is not None:
        if min.val > p.next.val:
            min = p.next
            befmin = p
        p = p.next

    if min != first:
        first = swap(first, first, min, befmin)

    first.next = selection_sort(first.next)

    return first


el = Node(6)
el.next = Node(23)
el.next.next = Node(7)
el.next.next.next = Node(3)
el.next.next.next.next = Node(7)
el.next.next.next.next.next = Node(23)
el.next.next.next.next.next.next = Node(74)
el.next.next.next.next.next.next.next = Node(545)
el.next.next.next.next.next.next.next.next = Node(5)

el = selection_sort(el)
wypisz(el)