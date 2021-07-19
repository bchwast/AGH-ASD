"""Rozwazmy ciag (a0, . . . , an−1) liczb naturalnych. Załózmy, ze został podzielony
na k spójnych podciagów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1). Przez wartosc i-go podciagu
rozumiemy sume jego elementów a przez najgorszy podciag rozumiemy podciag o najmniejszej wartosci (rozstrzygajac
remisy w dowolny sposób). Wartoscia podziału jest wartosc jego najgorszego podciagu. Zadanie
polega na znalezienie podziału ciagu (a0, . . . , an−1) o maksymalnej wartosci."""

# f(m , p) - największa wartość najgorszego podziału dzieląc p pierwszych liczb na m spójnych podciągów

# f(m, p) = max(min(f(p - i, m - 1), sum(j = i + 1, p)T[i])); 0 <= i <= p - m


def maximin(T, k):
    F = [[float("-inf")] * len(T) for _ in range(k)]

    temp = 0
    for i in range(len(T)):
        temp += T[i]
        F[0][i] = temp

    for m in range(1, k):
        for p in range(m, len(T)):
            c_sum = 0
            for i in range(p - 1, m - 2, -1):
                c_sum += T[i + 1]
                F[m][p] = max(F[m][p], min(F[m - 1][i], c_sum))

    return F[k - 1][len(T) - 1]


T = [1, 2, 3, 4, 5]
k = 3
print(maximin(T, k))