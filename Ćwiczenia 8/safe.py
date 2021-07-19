from queue import Queue

"""Dostałeś sejf, który odblokowuje się czterocyfrowym PINem (0000 - 9999). Pod wyświetlaczem znajduje się kilka
 przycisków z liczbami od 1 do 9999 - przykładowo (13, 223, 782, 3902). Sejf ten działa inaczej niż normalny: 
 wciśnięcie przycisku z liczbą powoduje dodanie liczby z przycisku do liczby na wyświetlaczu. Jeżeli suma jest większa 
 niż 9999, to pierwsza cyfra zostaje obcięta.
 Jest tobie znany PIN oraz cyfry, które są aktualnie wyświetlane. Znajdź najkrótszą sekwencję naciśnięć przycisków, 
 która pozwoli ci odblokować sejf. Jeżeli taka sekwencja nie istnieje, zwróć None.
"""

# tworzymy graf skierowany z wierzchołkami, które są kodami 0000 - 9999 i krawędziami takimi, że z jednego wierczchołka
# można przejść na drugi po naciśnięciu jednego przycisku, odpalamy bfs'a z początkowego kodu i znajdujemy najkrótszą
# ścieżkę do kodu PIN


def safe(buttons, start, pin):
    def path(v):
        if v == start:
            return [start]
        return path(parent[v]) + [v]


    G = [[] for _ in range(10000)]
    for i in range(10000):
        for button in buttons:
            G[i].append((i + button) % 10000)

    visited = [False] * 10000
    parent = [None] * 10000
    Q = Queue()
    visited[start] = True
    Q.put(start)
    flag = True
    while not Q.empty() and flag:
        u = Q.get()
        for v in G[u]:
            if v == pin:
                flag = False
                parent[v] = u
                break
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.put(v)

    if flag:
        return None
    route = path(pin)

    for i in range(len(route) - 1):
        for button in buttons:
            if (route[i] + button) % 10000 == route[i + 1]:
                route[i] = button
                break
    route.pop()
    return route


buttons = [13, 223, 782, 3902]
start = 2137
pin = 420
print(safe(buttons, start, pin))