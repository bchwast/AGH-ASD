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


def print_list(L):
    while L != None:
        print(L.value, end=" -> ")
        L = L.next
    print("|")


def fixSortedList(L):
    first = L
    second = L.next

    if first.value > second.value:
        wrong = first
        L = second
    else:
        while second != None:
            if second.value < first.value:
                wrong = second
                first.next = second.next
                break
            else:
                first = second
                second = second.next

    head = Node()
    head.next = L
    tail = head

    while tail.next.value < wrong.value:
        tail = tail.next

    wrong.next = tail.next
    tail.next = wrong

    return head.next


T = [2, 4, 6, 5, 8, 10]
L = tab2list(T)
L = fixSortedList(L)
print_list(L)