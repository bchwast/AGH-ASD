"""Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą być zarówno dodatnie
 jak i ujemne). Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności,
 by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartość końcowej sumy
 również traktujemy jak wynik tymczasowy) był możliwie jak najmniejszy.

 Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie wybiera kolejność dodawań.
 Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie;
 zakładamy, że tablica zawiera co najmniej dwie liczby) i zwraca największą wartość bezwzględną wyniku tymczasowego
 w optymalnej kolejności dodawań.

 Na przykład dla tablicy wejściowej: [1,−5, 2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a
 następnie dodaniu 1 do wyniku. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową.
"""

# f(i, j) - największa wartość bezwzględna wyniku tymczasowego pray dodawaniu liczb od ni do nj

# f(i, i + 1) = abs(ni + n(i + 1))
# f(i, j) = max(abs(ni + nj), min(f(i, j - 1), f(i + 1, j))) ; j > i + 1


def sumpr(low, high, pref):
    return pref[high + 1] - pref[low]


def opt(T):
    n = len(T)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + T[i]

    F = [[float("-inf")] * n for _ in range(n)]
    for i in range(1, n):
        F[i - 1][i] = abs(sumpr(i - 1, i, pref))

    for j in range(2, n):
        for i in range(j - 1, -1, -1):
            F[i][j] = max(abs(sumpr(i, j, pref)), min(F[i][j - 1], F[i + 1][j]))

    return F[0][n - 1]


T = [1, -5, 2, 3, -8, 6]
print(opt(T))
