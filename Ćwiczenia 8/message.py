"""Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n - 1.
 Dnia pierwszego osoba 0 przekazuje pewną wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych
 przekazuje tę wiadomość wszystkim swoim znajomym, którzy jej jeszcze nie znali, i tak dalej.
 Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ją otrzymały.
"""

# używamy bfs'a, w którym jawnie oddzielamy pojedyncze fale i zliczamy ile wierzchołków odwiedziliśmy podczas danej fali


from queue import Queue


def graphize(T):
    T.sort()
    n = max(T[len(T) - 1][0], T[len(T) - 1][1]) + 1
    G = [[] for _ in range(n)]
    for i in range(len(T)):
        G[T[i][0]].append(T[i][1])
        G[T[i][1]].append(T[i][0])
    return G


def message(G, s):
    m_day = day = 1
    m_amm = amm = 0
    n = len(G)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    Q.put(None)

    while not Q.empty():
        u = Q.get()
        if u is None:
            if amm > m_amm:
                m_amm = amm
                m_day = day
            amm = 0
            day += 1
            if not Q.empty():
                Q.put(None)
        else:
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    amm += 1
                    Q.put(v)

    return m_day, m_amm


G = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [1, 6], [2, 7], [3, 8], [4, 5], [4, 7], [5, 6], [5, 7], [6, 7], [8, 9]]
graph = graphize(G)
start = 0
print(message(graph, start))