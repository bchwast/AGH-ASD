from e3_ex2_testy import runtests


def tower(A):
    longest = [1] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[i][1] <= A[j][1] and longest[j] + 1 > longest[i]:
                longest[i] = longest[j] + 1

    return max(longest)


runtests(tower)
