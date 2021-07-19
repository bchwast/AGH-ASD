from random import randint


def countsort(T, k):
    occurences = [0] * k
    result = [0] * len(T)

    for i in range(len(T)):
        occurences[T[i]] += 1

    for i in range(1, k):
        occurences[i] += occurences[i - 1]

    for i in range(len(T) - 1, -1, -1):
        occurences[T[i]] -= 1
        result[occurences[T[i]]] = T[i]

    for i in range(len(T)):
        T[i] = result[i]


T1 = [randint(0, 500) for _ in range(1000000)]
print(T1)
countsort(T1, 501)
print(T1)