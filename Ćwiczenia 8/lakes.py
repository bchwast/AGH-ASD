from queue import Queue

"""Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość “W” - reprezentującą wodę lub “L” - ląd. 
 Grupę komórek wody połączonych ze sobą brzegami nazywamy jeziorem.
 a) Policz, ile jezior jest w tablicy
 b) Policz, ile komórek zawiera największe jezioro
 c) Zakładając, że pola o indeksach [0][0] i [n-1][n-1] są lądem, sprawdź czy da się przejść drogą lądową z pola [0][0] 
    do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.
 d) Znajdź najkrótszą ścieżkę między tymi punktami. Wypisz po kolei indeksy pól w tej ścieżce
"""

# a) i b) przechodzimy po tablicy i zapuszczamy dfs'a w momencie trafienia na wodę, na każdym polu z wodą ustawiamy, że
# zostało odwiedzone


def lakes_ab(T):
    def dfs(i, j):
        nonlocal size
        visited[i][j] = True

        if i > 0 and T[i - 1][j] == "W" and not visited[i - 1][j]:
            size += 1
            dfs(i - 1, j)
        if j < n - 1 and T[i][j + 1] == "W" and not visited[i][j + 1]:
            size += 1
            dfs(i, j + 1)
        if i < n - 1 and T[i + 1][j] == "W" and not visited[i + 1][j]:
            size += 1
            dfs(i + 1, j)
        if j > 0 and T[i][j - 1] == "W" and not visited[i][j - 1]:
            size += 1
            dfs(i, j - 1)


    n = len(T)
    lakes = 0
    size = m_size = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if T[i][j] == "L":
                visited[i][j] = True
            else:
                if not visited[i][j]:
                    size = 1
                    dfs(i, j)
                    m_size = max(m_size, size)
                    lakes += 1

    return lakes, m_size


# c) i d) odpalamy bfs'a w polu [0][0] i sprawdzamy czy odwiedziliśmy [n - 1][n - 1], budujemy ścieżkę przechodząc po
# parentach od [n - 1][n - 1]


def lakes_cd(T):
    def path(i, j):
        if i == 0 and j == 0:
            return [[0, 0]]
        return path(parent[i][j][0], parent[i][j][1]) + [[i, j]]


    n = len(T)
    visited = [[False] * n for _ in range(n)]
    parent = [[None, None] * n for _ in range(n)]
    Q = Queue()
    Q.put([0, 0])
    visited[0][0] = True

    while not Q.empty():
        u = Q.get()
        if u[0] > 0 and T[u[0] - 1][u[1]] == "L" and not visited[u[0] - 1][u[1]]:
            visited[u[0] - 1][u[1]] = True
            parent[u[0] - 1][u[1]] = u
            Q.put([u[0] - 1, u[1]])
        if u[1] < n - 1 and T[u[0]][u[1] + 1] == "L" and not visited[u[0]][u[1] + 1]:
            visited[u[0]][u[1] + 1] = True
            parent[u[0]][u[1] + 1] = u
            Q.put([u[0], u[1] + 1])
        if u[0] < n - 1 and T[u[0] + 1][u[1]] == "L" and not visited[u[0] + 1][u[1]]:
            visited[u[0] + 1][u[1]] = True
            parent[u[0] + 1][u[1]] = u
            Q.put([u[0] + 1, u[1]])
        if u[1] > 0 and T[u[0]][u[1] - 1] == "L" and not visited[u[0]][u[1] - 1]:
            visited[u[0]][u[1] - 1] = True
            parent[u[0]][u[1] - 1] = u
            Q.put([u[0], u[1] - 1])

    if not visited[n - 1][n - 1]:
        return False

    route = path(n - 1, n - 1)
    return True, route


T = [["L", "W", "L", "L", "L", "L", "L", "L"], ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"], ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"], ["L", "W", "L", "L", "L", "L", "W", "W"],
     ["W", "W", "L", "W", "W", "L", "W", "L"], ["L", "L", "L", "W", "L", "L", "L", "L"]]
print(lakes_ab(T))
print(lakes_cd(T))