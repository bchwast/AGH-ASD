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
    return head


def print_list(L):
    while L != None:
        print(L.value, end=" -> ")
        L = L.next
    print("|")


def get_len(L):
    cnt = -1
    while L != None:
        L = L.next
        cnt += 1
    return cnt


def insert_node(L, node):
    head = L
    while L.next != None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node
    return head


def get_tail(L):
    while L.next != None:
        L = L.next
    return L


def Sort(L):
    n = get_len(L)
    buckets = [Node() for _ in range(n)]
    bucket_range = 10 / n

    L = L.next
    while L != None:
        bucket = buckets[int(L.value // bucket_range)]
        el = L
        L = L.next
        bucket = insert_node(bucket, el)

    head = Node()
    tail = head

    for i in range(n):
        if buckets[i].next != None:
            current_tail = get_tail(buckets[i])
            tail.next = buckets[i].next
            tail = current_tail

    tail.next = None
    return head

T = [2, 6, 2, 0, 2.8, 5, 2, 9.9999999, 4.14, 3.14, 2.137, 2.115, 9]
L = tab2list(T)
print_list(L)
L = Sort(L)
print_list(L)