"""Wpewnym laboratorium genetycznym powstał ciag sekwencji DNA. Kazda sekwencja
to pewien napis składajacy sie z symboli G, A, T, i C. Przed dalszymi badaniami konieczne jest upewnic sie,
ze wszystkie sekwencje DNA sa parami rózne. Prosze opisac algorytm, który sprawdza czy tak faktycznie jest."""

# opis zbędny


class Node:
    def __init__(self):
        self.end = False
        self.A = None
        self.C = None
        self.G = None
        self.T = None


def check(root, seq, i):
    if i == len(seq):
        if root.end:
            return False
        root.end = True
        return True

    if seq[i] == "A":
        if root.A is None:
            root.A = Node()
        return check(root.A, seq, i + 1)
    elif seq[i] == "C":
        if root.C is None:
            root.C = Node()
        return check(root.C, seq, i + 1)
    elif seq[i] == "G":
        if root.G is None:
            root.G = Node()
        return check(root.G, seq, i + 1)
    else:
        if root.T is None:
            root.T = Node()
        return check(root.T, seq, i + 1)


def genes(G):
    n = len(G)
    root = Node()
    for i in range(n):
        if not check(root, G[i], 0):
            return False
    return True


G = ["ACG", "ACGT", "ACC", "GTC", "ACC", "TGA"]
print(genes(G))
