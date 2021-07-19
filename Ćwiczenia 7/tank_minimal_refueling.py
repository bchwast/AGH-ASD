# wybieramy najbardziej oddaloną stację, którą możemy wybrać


def tank(S, L, t):
    S.append(t)
    n = len(S)

    fuel = L
    cnt = 0
    for i in range(n):
        if fuel - S[i] < 0:
            i -= 1
            cnt += 1
            fuel = L + S[i]

    return cnt


S = [5, 8, 12, 15, 27, 30, 43, 50]
t = 56
L = 15
print(tank(S, L, t))