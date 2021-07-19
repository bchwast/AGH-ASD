# 1.5 pkt

from kp1_ex1_testy import runtests


def trav_tree(T, L):
    if T is not None:
        trav_tree(T.left, L)
        L.append(T)
        trav_tree(T.right, L)


def ConvertTree(p):
    L = []
    trav_tree(p, L)
    n = len(L)

    for i in range(n):
        if (2 * i) + 1 < n:
            L[i].left = L[(2 * i) + 1]
            if (2 * i) + 2 < n:
                L[i].right = L[(2 * i) + 2]
            else:
                L[i].right = None
        else:
            L[i].left = None
            L[i].right = None

        if (i - 1) // 2 >= 0:
            L[i].parent = L[(i - 1) // 2]
        else:
            L[i].parent = None

    return L[0]


runtests( ConvertTree )