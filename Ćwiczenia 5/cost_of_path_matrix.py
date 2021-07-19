"""Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Nalezy przejsc z pola (1, 1) na pole (n,n) korzystajac jedynie z ruchów “w dół”
oraz “w prawo”. Wejscie na dane pole kosztuje tyle, co znajdujaca sie tam liczba. Prosze podac algorytm
znajdujacy trase o minimalnym koszcie."""

# f(i, j) - minimalny koszt dostania się z pola [0][0] na pole [i][j]

# f(0, 0) = 0
# f(i, 0) = sum(k = 0, i)A[k][0]
# f(0, j) = sum(k = 0, j)A[0][k]
# f(i, j) = min(f(i - 1, j), f(i, j - 1)) + A[i][j]


def print_solution(map, i, j):
    if map[i][j] == None:
        print(f"[{0}][{0}] -> [{i}][{j}]", end=" -> ")
        return
    print_solution(map, map[i][j][0], map[i][j][1])
    print(f"[{i}][{j}]", end=" -> ")


def cost_of_path(T):
    rows = len(T)
    columns = len(T[0])
    costs = [[0] * columns for _ in range(rows)]
    parents = [[None] * columns for _ in range(rows)]

    costs[0][0] = T[0][0]
    for i in range(1, columns):
        costs[0][i] = costs[0][i - 1] + T[0][i]
    for i in range(1, rows):
        costs[i][0] = costs[i - 1][0] + T[i][0]

    for i in range(1, rows):
        for j in range(1, columns):
            if costs[i - 1][j] < costs[i][j - 1]:
                costs[i][j] = costs[i - 1][j] + T[i][j]
                parents[i][j] = (i - 1, j)
            else:
                costs[i][j] = costs[i][j - 1] + T[i][j]
                parents[i][j] = (i, j - 1)

    return costs[rows - 1][columns - 1], parents


T = [[3, 4, 5, 2, 1], [7, 2, 13, 7, 8], [3, 1, 4, 6, 5], [2, 8, 11, 10, 3], [3, 5, 1, 6, 2]]
cost, map = cost_of_path(T)
print(cost)
print_solution(map, len(T) - 1, len(T) - 1)