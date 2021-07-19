# 2 pkt

from k3_ex3_testy import runtests
from k3_ex3_EK import edmonds_karp


def floyd_warshall(G):
    n = len(G)
    S = [[G[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:
                S[i][j] = float("inf")

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]

    return S


def BlueAndGreen(T, K, D):
    n = len(T)
    G = [[0] * (n + 2) for _ in range(n + 2)]
    S = floyd_warshall(T)

    for i in range(n):
        for j in range(n):
            if S[i][j] >= D and S[i][j] != float("inf"):
                if K[i] == "B" and K[j] == "G":
                    G[i][j] = 1
                    G[n][i] = 1
                    G[j][n + 1] = 1

    res = edmonds_karp(G, n, n + 1)
    return res


runtests( BlueAndGreen ) 
