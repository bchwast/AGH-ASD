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


def reverse_list(L):
    if L is None or L.next is None:
        return L

    pred = None
    curr = L
    succ = None

    while curr is not None:
        succ = curr.next
        curr.next = pred
        pred = curr
        curr = succ

    L = pred
    return L


T = [3, 4, 2, 5, 10, 12]
L = tab2list(T)
print_list(L)
L = reverse_list(L)
print_list(L)