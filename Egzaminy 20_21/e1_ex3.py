# 1 pkt

from e1_ex3_testy import runtests


def kintersect(A, k):
    n = len(A)
    T = [(i, A[i][0], A[i][1]) for i in range(n)]
    T.sort(key=lambda x: x[2], reverse=True)
    res = []
    max_l = float("-inf")

    if k == 1:
        res1 = [None]
        for i in range(n):
            if T[i][2] - T[i][1] > max_l:
                max_l = T[i][2] - T[i][1]
                res1[0] = T[i][0]
        return res1

    for i in range(n):
        tmp = []
        tmp.append(T[i][0])
        for j in range(n):
            if j == i:
                continue
            if T[j][1] <= T[i][1] and T[i][1] < T[j][2]:
                tmp.append(T[j][0])
                if len(tmp) == k:
                    r = min(T[j][2], T[i][2])
                    l = r - T[i][1]
                    if l > max_l:
                        max_l = l
                        res = []
                        for a in range(k):
                            res.append(tmp[a])
                    break

    return res






runtests(kintersect)
