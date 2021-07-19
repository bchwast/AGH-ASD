from copy import deepcopy


def get_solutions(T, F, i, s, res, result):
    if i == 0 and s != 0 and F[i + 1][s]:
        res.append(T[i])
        if T[i] == s:
            result.append(res)
        return
    if i == 0 and s == 0:
        result.append(res)
        return
    if F[i][s]:
        n_res = deepcopy(res)
        get_solutions(T, F, i - 1, s, n_res, result)
    if s >= T[i] and F[i][s - T[i]]:
        res.append(T[i])
        get_solutions(T, F, i - 1, s - T[i], res, result)


def tssum(T, target):
    n = len(T)
    F = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        F[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < T[i - 1]:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = (F[i - 1][j] or F[i - 1][j - T[i - 1]])

    if not F[n][target]:
        return None

    result = []
    get_solutions(T, F, n - 1, target, [], result)

    return result


T = [3, 14, 34, 4, 10, 1, 12, 5, 2]
print(tssum(T, 14))