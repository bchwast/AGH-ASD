from kp1_ex2_testy import runtests

class FastListNode:
    def __init__(self, a):
        self.a = a  # przechowywana liczba calkowita
        self.next = []  # lista odnosnikow do innych elementow; poczatkowo pusta

    def __str__(self):  # zwraca zawartosc wezla w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


def fast_list_prepend(L, a):
    if L is None:
        A = FastListNode(a)
        return A

    A = FastListNode(a)
    A.next.append(L)
    l = L
    i = 2
    p = 2
    while l.next != []:
        if i == p:
            A.next.append(l.next[0])
            p *= 2
        i += 1
        l = l.next[0]

    return A


runtests( fast_list_prepend ) 
