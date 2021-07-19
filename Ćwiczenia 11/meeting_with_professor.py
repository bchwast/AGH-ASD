from queue import PriorityQueue

"""Pewien znany profesor zaprosił Cię na spotkanie w Magicznym Mieście. W mieście tym niektóre drogi mogą być
 uczęszczane tylko przez ludzi poniżej 30 roku życia (w tym Ciebie), inne tylko przez ludzi w wieku od 30 lat 
 (w tym profesora). Są też drogi, które mogą być uczęszczane przez każdego. Każda z dróg ma określoną długość, 
 wyrażoną dodatnią liczbą naturalną, może być jedno- lub dwukierunkowa.
 Drogi te łączą możliwe lokalizacje spotkania. Wśród nich wyróżniamy mieszkanie Twoje i mieszkanie profesora.
 Profesor prosi Cię, byś wybrał takie miejsce na spotkanie, aby łączna droga, którą musicie pokonać Ty i profesor była 
 jak najmniejsza. Jeżeli jest więcej niż jedno takie miejsce, podaj je wszystkie. Jeżeli takie miejsce nie istnieje, 
 algorytm również powinien to stwierdzić."""

# Uruchamiamy algorytm Dijkstry z naszego mieszkania i poruszamy się tylko po ścieżkach dla młodych i wspólnych.
# Uruchamiamy algorytm Dijkstry z mieszkania profesora i poryszamy się tylko po ścieżkach dla starych i wspólnych.
# Sumujemy odległości do wszystkich wierzchołków i znajdujemy takie o najmniejszej sumie, jeżeli najmniejsza suma to
# nieskończoność, to miejsce spotkania nie istnieje


def relax(d, u, v, weight):
    if d[v] > d[u] + weight:
        d[v] = d[u] + weight


def dijkstra(G, s, m):
    n = len(G)
    d = [float("inf")] * n
    enqueued = [True] * n
    Q = PriorityQueue()

    d[s] = 0
    cnt = 0
    Q.put((d[s], s))
    while not Q.empty() and cnt < n:
        u = Q.get()[1]
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]] and (v[2] == 0 or v[2] == m):
                relax(d, u, v[0], v[1])
                Q.put((d[v[0]], v[0]))

    return d


def meeting_with_professor(G, s_p, p_p):
    n = len(G)
    d1 = dijkstra(G, s_p, 1)
    d2 = dijkstra(G, p_p, 2)
    d = [0] * n
    m_d = float("inf")
    for i in range(n):
        d[i] = d1[i] + d2[i]
        m_d = min(m_d, d[i])
    if m_d == float("inf") :
        return None
    places = []
    for i in range(n):
        if d[i] == m_d:
            places.append(i)
    return places