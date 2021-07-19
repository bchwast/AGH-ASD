from e0_ex1_testy import runtests
from collections import deque


def tanagram(x, y, t):
    n = len(x)
    letters = [deque() for _ in range(26)]

    for i in range(n):
        letters[ord(y[i]) - 97].append(i)

    for i in range(n):
        if len(letters[ord(x[i]) - 97]) == 0:
            return False
        else:
            ind = letters[ord(x[i]) - 97].popleft()
            if abs(i - ind) > t:
                return False

    return True

runtests( tanagram )