"""Dostajemy liczbę naturalną n. Naszym zadaniem jest policzenie wszystkich binarnych (0/1) stringów o długości n bez
jedynek obok siebie"""

# f(i) - ilość binarnych stringów długości i, bez jedynek obok siebie

# f(1) = 2
# f(2) = 3
# f(i) = f(i - 1) + f(i - 2)


def no_consecutive_1s(n):
    F = [None] * n
    F[0] = 2
    F[1] = 3
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]

    return F[n - 1]


print(no_consecutive_1s(10))