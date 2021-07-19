from random import *


def alloc(n):
    return [randint(0, 1000000000) for i in range(n)]


print(alloc(3))


def countsort(T, f):
    n = len(T)
    B = [0] * n
    C = [0] * n
    for i in range(n):
        C[f(T[i])] += 1
    for i in range(1, n):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[f(T[i])] -= 1
        B[C[f(T[i])]] = T[i]
    for i in range(n):
        T[i] = B[i]


def sortnsq(T):
    n = len(T)
    countsort(T, lambda x: x % n)
    countsort(T, lambda x: x // n)


def sortnsquare(T):
    n = len(T)
    B = [0] * n
    C = [0] * n
    for i in range(n):
        C[T[i] % n] += 1
    for i in range(1, n):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[T[i] % n] -= 1
        B[C[T[i] % n]] = T[i]
    C = [0] * n
    D = [0] * n
    for i in range(n):
        C[B[i] // n] += 1
    for i in range(1, n):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        C[B[i] // n] -= 1
        D[C[B[i] // n]] = B[i]
    for i in range(n):
        T[i] = D[i]
    return T


n = 10
T = [randint(0, n ** 2 - 1) for i in range(n)]
s = "kot"
''' print(s)
print(s[0])
print(ord(s[0])) '''


# print(T)
# sortnsq(T)
# print(T)


def check_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False

    counters = alloc(2 ** 16)

    for i in range(len(word1)):
        counters[ord(word1[i])] = 0

    for i in range(len(word1)):
        counters[ord(word1[i])] += 1
        counters[ord(word2[i])] -= 1

    for i in range(len(word1)):
        if counters[ord(word1[i])] != 0:
            return False

    return True


word1 = "absc*/^f4c9dd*de0gf"
word2 = "fegf/ds^dc09b*add*4"

print(check_anagrams(word1, word2))


def sort(A):
    for j in range(len(A)):
        for i in range(1, len(A), 1):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]


def maxspan(A):
    n = len(A)
    min_ = A[0]
    max_ = A[0]
    for i in range(n):
        min_ = min(min_, A[i])
        max_ = max(max_, A[i])

    B = [[] for _ in range(n)]
    x = (max_ + min_) / n

    for i in range(n):
        d = int((A[i] - min_) / x)
        B[d].append(A[i])

    result = 0
    prev_max = max(B[0])
    for i in range(1, n):
        if len(B[i]) != 0:
            act_min = min(B[i])
            result = max(result, act_min - prev_max)
            prev_max = max(B[i])

    return result


A = [0.5, 0.3, 0.01, 0.7, 0.2, 0.92, 0.11, 0.91]
res = maxspan(A)
print(res)
A.sort()
print(A)
