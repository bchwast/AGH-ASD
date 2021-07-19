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


def insert(first, el):
    if first is None or first.val > el.val:
        el.next = first
        first = el
    else:
        p = first
        while p.next is not None and p.next.val < el.val:
            p = p.next

        el.next = p.next
        p.next = el

    return first


def insertion_sort(first):
    if first is None or first.next is None:
        return first

    head = None

    p = first
    while p is not None:
        r = p.next
        head = insert(head, p)
        p = r

    first = head
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
el = insertion_sort(el)
wypisz(el)


