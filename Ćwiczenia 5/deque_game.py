"""Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną wartość z jednego z końców tablicy i dodajemy
 do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie, jaką maksymalną sumę
  możemy uzbierać?
“Uogólniony problem paczki mentosów”
"""

# f(i, j) - maksymalna suma jaką możemy uzbierać dla tablicy od i do j

# f(i, j) = max(T[i] + min(f(i + 2, j), f(i + 1, j - 1)), T[j] + min(f(i + 1, j - 1), f(i, j - 2))) ; o ile mamy na tyle
#                                                                                                     tablicy


def optimal_strategy(T):
    n = len(T)
    solutions = [[0] * n for _ in range(n)]

    for gap in range(n):
        for right in range(gap, n):
            left = right - gap

            l2r = 0
            if left + 2 <= right:
                l2r = solutions[left + 2][right]

            l1r1 = 0
            if left + 1 <= right - 1:
                l1r1 = solutions[left + 1][right - 1]

            lr2 = 0
            if left <= right - 2:
                lr2 = solutions[left][right - 2]

            solutions[left][right] = max(T[left] + min(l2r, l1r1), T[right] + min(l1r1, lr2))

    return solutions[0][n - 1]


T = [2, 3, 1, 4, 6, 8, 1, 2]
print(optimal_strategy(T))