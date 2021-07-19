# 2 pkt

from queue import PriorityQueue
from kp2_ex3_testy import runtests


def common_digits(a, b):
    c_a = []
    c_b = []
    while a > 0:
        c_a.append(a % 10)
        a /= 10
    while b > 0:
        c_b.append(b % 10)
        b /= 10
    for i in range(len(c_a)):
        if c_a[i] in c_b:
            return True
    return False


def dijkstra(G, s, t):
    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight
            parent[v] = u

    n = len(G)
    d = [float("inf")] * n
    parent = [None] * n
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
            if enqueued[v[0]]:
                relax(u, v[0], v[1])
                Q.put((d[v[0]], v[0]))

    return d[t]


def find_cost(T):
    n = len(T)
    i_min = 0
    i_max = 0
    for i in range(n):
        if T[i] < T[i_min]:
            i_min = i
        elif T[i] > T[i_max]:
            i_max = i

    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if common_digits(T[i], T[j]):
                    G[i].append((j, abs(T[i] - T[j])))
                    G[j].append((i, abs(T[j] - T[i])))

    res = dijkstra(G, i_min, i_max)
    if res == float("inf"):
        return -1
    return res

runtests(find_cost) 
