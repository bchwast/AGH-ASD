from e3_ex3_testy import runtests
from queue import PriorityQueue


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def merge(lists):
    n = len(lists)
    Q = PriorityQueue()
    L = Node("|")
    tail = L
    ind = 0
    for i in range(n):
        if lists[i] is not None:
            Q.put((lists[i].val, ind, lists[i]))
            ind += 1

    while not Q.empty():
        node = Q.get()[2]
        if node.next is not None:
            Q.put((node.next.val, ind, node.next))
            ind += 1
        tail.next = node
        tail = node

    return L.next


runtests( merge )
