# 2 pkt

class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.f = None
        self.g = None


def trav(x, w):
    if x.f is not None:
        w[0] = max(w[0], x.f, x.g)
        return x.f
    best = 0
    s_best = 0
    for y in range(x.children):
        cand = trav(x.child[y][0], w) + x.child[y][1]
        if cand > best:
            s_best = best
            best = cand
        elif cand > s_best:
            s_best = cand
    x.f = best
    x.g = best + s_best
    w[0] = max(w[0], x.f, x.g)
    return x.f


def heavy_path(T):
    w = [0]
    _ = trav(T, w)
    return w[0]


arr = [Node() for _ in range(22)]
arr[0].children = 3
arr[0].child = [(arr[1], -7), (arr[2], 6), (arr[3], -3)]
arr[1].children = 2
arr[1].child = [(arr[4], 5), (arr[5], 2)]
arr[2].children = 1
arr[2].child = [(arr[6], -1)]
arr[3].children = 3
arr[3].child = [(arr[7], 11), (arr[8], 11), (arr[9], 8)]
arr[4].children = 3
arr[4].child = [(arr[10], -3), (arr[11], 8), (arr[12], 6)]
arr[6].children = 2
arr[6].child = [(arr[13], 11), (arr[14], 5)]
arr[7].children = 2
arr[7].child = [(arr[15], 5), (arr[16], 7)]
arr[8].children = 2
arr[8].child = [(arr[17], 2), (arr[18], 3)]
arr[9].children = 3
arr[9].child = [(arr[19], 4), (arr[20], -5), (arr[21], 3)]

A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]

print(heavy_path(arr[0]))