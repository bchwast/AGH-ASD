class Vertex:
    def __init__(self, val):
        self.vertices = []
        self.best = -1
        self.wo = -1
        self.val = val


def best(v):
    if v.best >= 0:
        return v.best

    value_1 = v.val
    for u in v.vertices:
        value_1 += wo(u)

    value_2 = wo(v)
    v.best = max(value_1, value_2)

    return v.best


def wo(v):
    if v.wo >= 0:
        return v.wo

    v.wo = 0
    for u in v.vertices:
        v.wo += best(u)

    return v.wo


# a = Vertex(25)
# b = Vertex(28)
# c = Vertex(10)
# d = Vertex(100)
# e = Vertex(1)
# f = Vertex(35)
# g = Vertex(15)
# h = Vertex(20)
# i = Vertex(29)
# j = Vertex(50)
# k = Vertex(0)
# l = Vertex(0)
# m = Vertex(0)
# n = Vertex(100)
# o = Vertex(17)
# p = Vertex(45)
# q = Vertex(2)
# r = Vertex(700)
# p.vertices = [q, r]
# i.vertices = [o, p]
# e.vertices = [k, l, m, n]
# d.vertices = [i, j]
# c.vertices = [f, g, h]
# b.vertices = [e]
# a.vertices = [b, c, d]

a = Vertex(7)
b = Vertex(3)
c = Vertex(5)
d = Vertex(100)
e = Vertex(13)
f = Vertex(17)
g = Vertex(19)
h = Vertex(23)
i = Vertex(29)
d.vertices = [h, i]
c.vertices = [g]
b.vertices = [e, f]
a.vertices = [b, c, d]

print(best(a))