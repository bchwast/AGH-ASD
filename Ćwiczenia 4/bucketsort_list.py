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


def getProperties(L):
    cnt = 0
    maxEl = float("-inf")
    minEl = float("inf")
    while L != None:
        if L.value > maxEl:
            maxEl = L.value

        if L.value < minEl:
            minEl = L.value

        L = L.next
        cnt += 1
    return cnt, minEl, maxEl


def insertNode(L, node):
    start = L
    while L.next != None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node
    return start


def bucketsort(L):
    lenL, minEl, maxEl = getProperties(L)
    bucketTab = [Node() for _ in range(lenL)]
    bucketRange = (maxEl - minEl) / lenL

    while L != None:
        bucket = bucketTab[min(int((L.value - minEl) / bucketRange), lenL - 1)]
        el = L
        L = L.next
        bucket = insertNode(bucket, el)

    head = Node()
    tail = head

    for i in range(lenL):
        while bucketTab[i].next != None:
            tail.next = bucketTab[i].next
            tail = tail.next
            bucketTab[i] = bucketTab[i].next

    tail.next = None
    return head.next


T = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
L = tab2list(T)
printList(L)
L = bucketsort(L)
printList(L)