"""Dostajemy na wejściu trzy stringi: A, B i C. A i B są tej samej długości. Zachodzą następujące właściwości:
 1) Litery na tym samym indeksie w stringach A i B są równoważne
 2) Jeżeli litera a jest równoważna z literą b, to litera b jest równoważna z literą a
 3) Jeżeli litera a jest równoważna z b, a litera b z literą c, to litera a jest równoważna z literą c
 4) Każda litera jest równoważna sama ze sobą

 W stringu C możemy zamienić dowolną literę z literą do niej równoważną. Jaki jest najmniejszy leksykograficznie string,
 który możemy w tej sposób skonstruować?"""

# tworzymy jednoelementowe zbiory rozłączne składające się z liter, łączymy w jeden zbiór litery równoważne,
# reprezentantem danego zbioru bedzie leksykograficznie najmniejsza zawarta w nim litera
# przechodząc jednocześnie po stringu A i B łączymy równoważne litery w zbiory
# przechodzimy po stringu C i tworzymy string będacy wynikiem


class Node:
    def __init__(self, val):
        self.val = val
        self.rank = ord(val)
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank < y.rank:
        y.parent = x
    else:
        x.parent = y


def equivalent_letters(A, B, C):
    let = [Node(chr(i)) for i in range(97, 123)]
    for i in range(len(A)):
        union(let[ord(A[i]) - 97], let[ord(B[i]) - 97])
    res = ""
    for i in range(len(C)):
        res += let[ord(C[i]) - 97].parent.val
    return res


print(equivalent_letters("abefz", "bceea", "abcdefgz"))