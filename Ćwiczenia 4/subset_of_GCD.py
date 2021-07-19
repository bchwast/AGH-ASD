from math import sqrt
from random import randint


def sieve(n):
    sieveT = [True] * n
    for i in range(2, int(sqrt(n)) + 1):
        if sieveT[i]:
            for j in range(i * i, n, i):
                sieveT[j] = False

    primes = []
    for i in range(2, n):
        if sieveT[i]:
            primes.append(i)

    return primes


def largest_subset(T):
    n = len(T)
    primes = sieve(n)

    occurences = [0] * len(primes)

    for i in range(n):
        for j in range(len(primes)):
            if T[i] >= primes[j] and T[i] % primes[j] == 0:
                occurences[j] += 1

    return max(occurences)

n = 20
T = [randint(0, n - 1) for _ in range(n)]
print(T)
print(largest_subset(T))