"""Dane jest drzewo ukorzenione T, gdzie kazdy wierzchołek v ma—
potencjalnie ujemna—wartosc value(v). Prosze zaproponowac algorytm, który znajduje wartosc najbardziej
wartosciowej sciezki w drzewie T."""

# f(v) - wartość najbardziej wartościowej ścieżki zaczynającej się na v i kierującej się w stronę liści

# f(v) = max(0, v.val, v.val + f(v.left), v.val + f(v.right))


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.path = 0


def path(v):
    if v == None:
        return (0, 0)
    l, ml = path(v.left)
    r, mr = path(v.right)

    v.path = max(0, v.val, v.val + l, v.val + r)
    m = max(ml, mr, v.path)
    return v.path, m


a = Node(10)
b = Node(7)
c = Node(5)
d = Node(8)
e = Node(-100)
f = Node(2)
g = Node(1)
h = Node(-7)
i = Node(20)
j = Node(7)
k = Node(-5)
l = Node(1)
m = Node(-4)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
d.left = g
d.right = h
f.left = i
f.right = j
g.left = k
h.right = l
k.left = m


x, y = path(a)
print(y)