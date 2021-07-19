# zakładamy, że wierzchołki możemy ponumerować od 0 do n - 1.
# tworzymy macierz A rozmiaru n x n, która początkowo zawiera same wartości None
# dla wszystkich wierzchołków i oraz dla wszystkich par j i k sąsiadujących z nimi wierzchołków sprawdzamy czy A[j][k]
# ma wartość None, jeżeli tak to nadajemy jej wartość i, jeżeli posiada już jakąś wartość to znaleźliśmy cykl długości 4
# w najgorszym przypadku rozpatrzymy wszystkie możliwe pary wierzchołków, jest ich (n po 2) oraz tworzymy macierz n x n
# zatem złożoność czasowa wyniesie O(n^2).


def find_4_cycle(G):
    n = len(G)
    A = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(len(G[i])):
            for k in range(j + 1, len(G[i])):
                if A[G[i][j]][G[i][k]] == None or A[G[i][k]][G[i][j]] == None:
                    A[G[i][j]][G[i][k]] = i
                    A[G[i][k]][G[i][j]] = i
                elif A[G[i][j]][G[i][k]] == i or A[G[i][k]][G[i][j]] == i:
                    continue
                else:
                    return [G[i][j], i, G[i][k], A[G[i][j]][G[i][k]]]

    return None


G = [[1, 5], [0, 2, 4, 5], [1, 3, 4, 5], [2, 4], [3, 2, 1, 5], [0, 1, 2, 4]]
print(find_4_cycle(G))