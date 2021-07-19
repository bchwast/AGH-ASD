import timeit
from random import randint


def sortn2_1(T):
    n = len(T)

    occurences = [0] * n
    temp = [0] * n

    for i in range(n):
        occurences[T[i] % n] += 1
    for i in range(1, n):
        occurences[i] += occurences[i - 1]
    for i in range(n - 1, -1, -1):
        occurences[T[i] % n] -= 1
        temp[occurences[T[i] % n]] = T[i]

    occurences = [0] * n
    result = [0] * n

    for i in range(n):
        occurences[temp[i] // n] += 1
    for i in range(1, n):
        occurences[i] += occurences[i - 1]
    for i in range(n - 1, -1, -1):
        occurences[temp[i] // n] -= 1
        result[occurences[temp[i] // n]] = temp[i]

    for i in range(n):
        T[i] = result[i]


n = 10
T = [randint(0, n*n - 1) for _ in range(n)]
print(T)
start = timeit.default_timer()
sortn2_1(T)
stop = timeit.default_timer()
print(T)
print(stop - start)