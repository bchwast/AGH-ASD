def path(P, i, j):
    if P[i][j] == i:
        return [i, j]
    return path(P, i, P[i][j]) + [j]


def floyd_warshall(G):
    n = len(G)
    S = [[G[i][j] for j in range(n)] for i in range(n)]
    P = [[i] * n for i in range(n)]

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]
                    P[u][w] = P[t][w]

    return S, P


G = [[float("inf"), 1, float("inf"), float("inf"), 5],
     [1, float("inf"), 7, 8, 2],
     [float("inf"), 7, float("inf"), 1, float("inf")],
     [float("inf"), 8, 1, float("inf"), 3],
     [5, 2, float("inf"), 3, float("inf")]]
S, P = floyd_warshall(G)
print(path(P, 0, 2))
