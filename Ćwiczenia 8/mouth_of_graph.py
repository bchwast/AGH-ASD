"""Mówimy, ze wierzchołek t w grafie skierowanym jest uniwersalnym
 ujsciem, jesli (a) z kazdego innego wierzchołka v istnieje krawedz z v do t, oraz (b) nie istnieje zadna krawedz
 wychodzaca z t."""

# trzymamy na stosie dwa wierzchołki (p, q), jeżeli istnieje krawędź z p do q, to p na pewno nie jest ujściem i go
# odrzucamy, jeżeli nie istnieje krawędź z p do q, to q na pewno nie jest ujściem i go odrzucamy. po przejściu wszystkich
# wierzchołków zostanie nam jeden kandydat na ujście. teraz wystarczy sprawdzić, przechodząc po wszystkich wierzchołkach,
# czy nasz kandydat spełnia warunki na bycie uniwersalnym ujściem


def mouth(G):
    n = len(G)
    cand = [0, None]

    for u in range(1, n):
        if cand[0] is None:
            cand[0] = u
        else:
            cand[1] = u

        if G[cand[0]][cand[1]]:
            cand[0] = None
        else:
            cand[1] = None

    if cand[0] is not None:
        c = cand[0]
    else:
        c = cand[1]


    for u in range(n):
        if u == c:
            continue
        if not G[u][c] or G[c][u]:
            return None

    return c


G = [[0, 1, 1, 0, 1, 0],
     [0, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 1, 1],
     [0, 1, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 1, 0]]
print(mouth(G))
