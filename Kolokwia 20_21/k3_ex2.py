from k3_ex2_testy import runtests


class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def solution(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return float("inf")

    val = float("inf")
    if root.parent is not None:
        val = root.value

    val = min(val, solution(root.left) + solution(root.right))

    return val

def cutthetree(T):
    return solution(T)


    
runtests(cutthetree)


