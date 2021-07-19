class TNode:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.left = None
        self.right = None
        self.parent = None


def insert(root, block):
    while root is not None:
        if block[0] > root.b or block[1] < root.a:
            node = TNode(block[0], block[1], root.c + block[2])
            root.left = node
            return
        elif root.right is not None:
            root.a = min(root.a, block[0])
            root.b = max(root.b, block[1])
            root = root.right
        else:
            root.a = min(root.a, block[0])
            root.b = min(root.b, block[1])
            node = TNode(block[0], block[1], root.c + block[2])
            root.right = node
            return


def get_max(root):
    if root is None:
        return float("-inf")
    return max(get_max(root.left), get_max(root.right), root.c)


def block_height(K):
    n = len(K)
    root = TNode(float("-inf"), float("inf"), 0)
    for i in range(n):
        insert(root, K[i])

    res = get_max(root)
    return res


K1 = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
R1 = 5

K2 = [(1, 3, 1), (2, 4, 1), (3, 5, 1), (4, 6, 1), (5, 7, 1), (6, 8, 1)]
R2 = 6

K3 = [(1, 10 ** 10, 1)]
R3 = 1

TESTY = [(K1, R1), (K2, R2), (K3, R3)]

good = True
for KK, RR in TESTY:
    print("Klocki           : ", KK)
    print("Oczekiwany wynik : ", RR)
    WW = block_height(KK)
    print("Otrzymany wynik  : ", WW)
    if WW != RR:
        print("Błąd!!!!")
        good = False

if good:
    print("OK!")
else:
    print("Problemy!")
