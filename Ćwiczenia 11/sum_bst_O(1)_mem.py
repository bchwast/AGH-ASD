"""Prosze zapropnowac algorytm, który oblicza sume wszystkich wartosci w drzewie binarnym zdefiniowanym na wezłach typu:
 class BNode:
     def __init__( self, val ):
         self.left = None
         self.right = None
         self.parent = None
         self.value = val
 Program moze korzystac wyłacznie ze stałej liczby zmiennych (ale wolno mu zmieniac strukture drzewa, pod warunkiem,
 ze po zakonczonych obliczeniach drzewo zostanie przywrócone do stanu poczatkowego.)"""

# znajdujemy minimum i idziemy po następnikach


class BNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def min_node(root):
    prev = None
    while root is not None:
        prev = root
        root = root.left
    return prev


def succ(root):
    if root.right is not None:
        return min_node(root.right)
    prev = root.parent
    while prev is not None and prev.right == root:
        root = prev
        prev = root.parent
    return prev


def bst_sum(root):
    res = 0
    start = min_node(root)
    while start is not None:
        res += start.val
        start = succ(start)
    return res