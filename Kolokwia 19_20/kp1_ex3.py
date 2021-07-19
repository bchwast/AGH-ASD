from kp1_ex3_testy import runtests

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.cnt = 1


def find(root, key):
    while root is not None:
        if root.key == key:
            if root.cnt > 1:
                root.cnt -= 1
                return False
            if root.cnt == 1:
                root.cnt -= 1
                return True
        elif key < root.key:
            root = root.left
        else:
            root = root.right


def insert(root, key):
    prev = None
    side = None
    while root is not None:
        if root.key == key:
            if root.cnt == 0:
                root.cnt += 1
                return True
            root.cnt += 1
            return False
        prev = root
        if key < root.key:
            root = root.left
            side = 0
        else:
            root = root.right
            side = 1
    node = BSTNode(key)
    node.parent = prev
    if side == 0:
        prev.left = node
    else:
        prev.right = node
    return True


def longest_incomplete( A, k ):
    n = len(A)
    t = BSTNode(-1)

    m, curr, diff = 0, 0, 0
    for i in range(n):
        if insert(t, A[i]):
            diff += 1
        if diff < k:
            curr += 1
            m = max(m, curr)
        else:
            while diff == k:
                if find(t, A[i - curr]):
                    diff -= 1
                else:
                    curr -= 1

    return m


runtests( longest_incomplete ) 
