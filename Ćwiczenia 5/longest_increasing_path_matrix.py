"""Dostajemy tablicę (M x N) wypełnioną wartościami. Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy
 (możemy przechodzić na pola sąsiadujące krawędziami), o rosnących wartościach (to znaczy, że z pola o wartości 3,
  mogę przejść na pola o wartości większej bądź równej 4)."""

# f(i, j) - długość najdłuższej ścieżki zaczynającej się w (i, j)

# początkowo dla każedego i, j - f(i, j) = 1
# f(i, j) = max(f(i - 1, j), f(i, j + 1), f(i + 1, j), f(i, j - 1)) + 1 ; o ile nie wychodzimy z tablicy i przechodzimy
#                                                                        na pole o większej wartości


def path(T, lengths, i, j):
    if lengths[i][j] > -1:
        return lengths[i][j]

    case_1 = case_2 = case_3 = case_4 = 0
    switch = False
    if i - 1 >= 0 and T[i - 1][j] > T[i][j]:
        case_1 = lengths[i - 1][j] = path(T, lengths, i - 1, j)
        switch = True
    if i + 1 < len(T) and T[i + 1][j] > T[i][j]:
        case_2 = lengths[i + 1][j] = path(T, lengths, i + 1, j)
        switch = True
    if j - 1 >= 0 and T[i][j - 1] > T[i][j]:
        case_3 = lengths[i][j - 1] = path(T, lengths, i, j - 1)
        switch = True
    if j + 1 < len(T[0]) and T[i][j + 1] > T[i][j]:
        case_4 = lengths[i][j + 1] = path(T, lengths, i, j + 1)
        switch = True

    if switch:
        return max(case_1, case_2, case_3, case_4) + 1
    return 0


def paths(T):
    rows = len(T)
    columns = len(T[0])
    lengths = [[-1] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            lengths[i][j] = path(T, lengths, i, j)

    longest = 0
    for i in range(rows):
        for j in range(columns):
            if lengths[i][j] > longest:
                longest = lengths[i][j]


    return longest

T = [[3, 4, 5, 2, 1], [7, 2, 13, 7, 8], [3, 1, 4, 6, 5], [2, 8, 11, 10, 3], [3, 5, 1, 6, 2]]
print(paths(T))
