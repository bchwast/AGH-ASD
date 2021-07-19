def findCandidate(T):
    count = 1
    cand = 0
    for i in range(len(T)):
        if T[i] == T[cand]:
            count += 1
        else:
            count -= 1

        if count == 0:
            cand = i
            count = 1

    return T[cand]


def isLeader(T, cand):
    count = 0
    for i in range(len(T)):
        if T[i] == cand:
            count += 1

    if count > len(T)//2:
        return True
    return False


def leader(T):
    if isLeader(T, findCandidate(T)):
        return True
    return False


T = [2,1,2,3,2,4,2]
print(leader(T))