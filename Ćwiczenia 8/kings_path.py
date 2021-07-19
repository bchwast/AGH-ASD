from queue import Queue

"""Dana jest szachownica o wymiarach n × n. Kazde pole (i, j)
ma koszt (liczbe ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings_path(A), która oblicza koszt
sciezki króla. Funkcja powinna byc mozliwie jak najszybsza"""

# puszczamy bfs'a z wagami równymi kosztowi pola, jeżeli koszt pola wynosi 1 to możemy przejść na nie w tej fali,
# jeżeli więcej to zmniejszamy koszt o 1 i wrzucamy spowrotem do kolejki


def kings_path(A):
    n = len(A)
    dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    Q = Queue()
    Q.put([0, 0, 1])
    Q.put(None)
    cost = A[0][0]

    while not Q.empty():
        u = Q.get()
        if u is None:
            cost += 1
            Q.put(None)
        elif u[2] > 1:
            u[2] -= 1
            Q.put(u)
        elif u[0] == n - 1 and u[1] == n - 1:
            return cost
        else:
            for i in range(8):
                if 0 <= u[0] + dirs[i][0] < n and 0 <= u[1] + dirs[i][1] < n:
                    v = [u[0] + dirs[i][0], u[1] + dirs[i][1], A[u[0] + dirs[i][0]][u[1] + dirs[i][1]]]
                    Q.put(v)
    return


A = [[1, 1, 1],
     [2, 4, 1],
     [1, 4, 1]]
print(kings_path(A))
