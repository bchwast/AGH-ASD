class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def print_list(L):
    while L is not None:
        print(L.val, end=" -> ")
        L = L.next
    print()


def tab2list(T):
    n = len(T)
    head = Node("|")
    tail = head
    for i in range(n):
        tmp = Node(T[i])
        tail.next = tmp
        tail = tail.next

    return head.next


def insert(L, el):
    if not L or L.val > el.val:
        el.next = L
        L = el
    else:
        curr = L
        while curr.next is not None and curr.next.val < el.val:
            curr = curr.next

        el.next = curr.next
        curr.next = el

    return L


def insertion_sort(L):
    if L is None or L.next is None:
        return L

    head = None
    curr = L
    while curr is not None:
        tmp = curr.next
        curr.next = None
        head = insert(head, curr)
        curr = tmp

    L = head
    return L


T = [4, 3, 2, 10, 12, 1, 5, 6]
L = tab2list(T)
print_list(L)
L = insertion_sort(L)
print_list(L)