from k2_ex3_testy import runtests
from queue import PriorityQueue


def dfs(T, i, j, n, m, fuel):
    fuel[0] += T[i][j]
    T[i][j] = 0

    if i > 0 and T[i - 1][j] > 0:
        dfs(T, i - 1, j, n, m, fuel)
    if j < m - 1 and T[i][j + 1] > 0:
        dfs(T, i, j + 1, n, m, fuel)
    if i < n - 1 and T[i + 1][j] > 0:
        dfs(T, i + 1, j, n, m, fuel)
    if j > 0 and T[i][j - 1] > 0:
        dfs(T, i, j - 1, n, m, fuel)


def plan(T):
    n = len(T)
    m = len(T[0])
    stain = [0]
    Q = PriorityQueue()
    res = []
    fuel = 0

    for j in range(m):
        if T[0][j] > 0:
            stain[0] = 0
            dfs(T, 0, j, n, m, stain)
            T[0][j] = stain[0]

    for j in range(m - 1):
        if T[0][j] > 0:
            Q.put((-1 * T[0][j], j))
        if fuel == 0:
            bonus = Q.get()
            fuel = -1 * bonus[0]
            res.append(bonus[1])
        fuel -= 1

    res.sort()
    return res


runtests(plan)
