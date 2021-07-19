"""Dane: ciąg liczb A[0], ..., A[n - 1]
   Zadanie: Znaleźć długość najdłuższego podciągu rosnącego"""

# f(i) - długość najdłuższego podciąg rosnącego kończącego się na A[i]

# f(0) = 1
# f(i) = max(f(i - k)) + 1; 1 <= k <= i; A[i - k] < A[i]


def lis(T):
    longest = [1] * len(T)
    parent = [-1] * len(T)
    for i in range(1, len(T)):
        for j in range(i):
            if T[j] < T[i] and longest[j] + 1 > longest[i]:
                parent[i] = j
                longest[i] = longest[j] + 1

    return max(longest), longest, parent


def print_solution(T, parent, i):
    if parent[i] != -1:
        print_solution(T, parent, parent[i])
    print(T[i])


T = [13, 7, 21, 42, 8, 2, 44, 53]

res, longest, parent = lis(T)
print(res, longest, parent)
print_solution(T, parent, longest.index(res))