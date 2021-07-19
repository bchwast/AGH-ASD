"""Wyjeżdżacie ze znajomymi na wakacje. Macie dwa samochody i N bagaży o łącznej wadze W. Waga każdego z bagaży jest
 liczbą naturalną dodatnią. Czy jesteście w stanie tak je zapakować, aby w obu samochodach były bagaże o tej
 samej łącznej wadze?"""

# Szukamy podciągu sumującego się do W/2

def tssum(T, W):
    if W % 2 != 0:
        return False

    target = W // 2
    n = len(T)
    F = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        F[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < T[i - 1]:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = (F[i - 1][j] or F[i - 1][j - T[i - 1]])

    return F[n][target]