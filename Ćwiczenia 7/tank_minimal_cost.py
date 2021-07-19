# tankujemy tyle, żeby móc dojechać do pierwszej stacji o tańszej benzynie, jeżeli nasz bak nie ma takiej pojemności,
# żeby móc dotrzeć do stacji o tańszej benzynie lub jesteśmy na stacji o najtańszej benzynie to tankujemy do pełna


def tank(S, P, L, t):
    n = len(S) + 2
    stations = [[None, None] for _ in range(n)]
    stations[0][0], stations[0][1] = 0, 0

    for i in range(1, n - 1):
        stations[i][0], stations[i][1] = S[i - 1], P[i - 1]
    stations[n - 1][0], stations[n - 1][1] = t, 0

    fuel = 0
    cost = 0
    for i in range(n - 1):
        if i > 0:
            fuel -= (stations[i][0] - stations[i - 1][0])
        min_cost = stations[i][1]
        st = i
        for j in range(i, n):
            if stations[j][0] > stations[i][0] + L:
                break
            else:
                if stations[j][1] < min_cost:
                    min_cost, st = stations[j][1], j
                    break
        if st == i:
            print(f"i {i} st {st} cost {cost} fuel {fuel}")
            cost += min(L - fuel, (t - stations[i][0]) - fuel) * stations[i][1]
            fuel = L
        else:
            print(f"i {i} st {st} cost {cost} fuel {fuel}")
            cost += max(((stations[st][0] - stations[i][0]) - fuel) * stations[i][1], 0)
            fuel = max(fuel, stations[st][0] - stations[i][0])

    return cost


L = 10
S = [8, 11, 15, 16]
P = [40, 7, 15, 12]
t = 23
print(tank(S, P, L, t))


