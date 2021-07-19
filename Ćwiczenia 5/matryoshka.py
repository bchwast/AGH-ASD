"""Sasza kolekcjonuje rosyjskie lalki - matrioszki. Każda z nich ma określoną wysokość X i szerokość Y, dane liczbami
 naturalnymi dodatnimi. Jedną matrioszkę można włożyć do drugiej, jeżeli ma od niej mniejszą zarówno wysokość, jak i szerokość.

 Sasza zastanawia się, jaki jest najdłuższy ciąg matrioszek, które może powkładać w siebie po kolei.
 Pomóż mu znaleźć odpowiedź na to pytanie.
"""

# f(i) - najdłuższy ciąg matrioszek z zewnętrzną i

# sortujemy matrioszki rosnąco po jednym wymiarze i wykonujemy lisa po drugiej patrząc czy się mieszczą


def get_index(A, tails, low, high, value):
    if 1 < high - low:
        mid = (high + low) // 2

        if A[tails[mid]][1] == value:
            return mid
        elif A[tails[mid]][1] > value:
            return get_index(A, tails, low, mid, value)
        else:
            return get_index(A, tails, mid, high, value)
    return high


def get_solution(parent, ind):
    if parent[ind] == -1:
        return [ind]
    return get_solution(parent, parent[ind]) + [ind]


def matryoshka(A):
    n = len(A)
    A.sort(key=lambda x: x[0])

    tails = [0] * n
    parent = [-1] * n
    l = 1

    for i in range(1, n):
        if A[i][1] < A[tails[0]][1]:
            tails[0] = i
        elif A[tails[l - 1]][1] < A[i][1]:
            tails[l] = i
            parent[i] = tails[l - 1]
            l += 1
        else:
            pos = get_index(A, tails, 0, l - 1, A[i][1])
            tails[pos] = i
            parent[i] = tails[pos - 1]

    result = get_solution(parent, tails[l - 1])
    return result


A = [(0, 3), (0, 5), (0, 1), (0, 8), (0, 2), (0, 4), (0, 7), (0, 6), (0, 1), (0, 3)]
print(matryoshka(A))
