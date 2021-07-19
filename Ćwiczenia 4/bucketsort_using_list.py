class Node:
    def __init__(self):
        self.value = None
        self.next = None


def insertNode(L, el):
    node = Node()
    node.value = el

    start = L
    while L.next != None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node
    return start


def bucketsort(T):
    maxEl, minEl = max(T), min(T)
    bucketTab = [Node() for _ in range(len(T))]
    bucketRange = (maxEl - minEl) / len(T)

    for i in range(len(T)):
        bucket = bucketTab[min(int((T[i] - minEl) / bucketRange), len(T) - 1)]
        bucket = insertNode(bucket, T[i])

    ind = 0
    for i in range(len(T)):
        while bucketTab[i].next != None:
            T[ind] = bucketTab[i].next.value
            bucketTab[i] = bucketTab[i].next
            ind += 1


T = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
bucketsort(T)
print(T)

