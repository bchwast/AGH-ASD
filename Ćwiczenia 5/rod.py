"""Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje. Kawałki mają długość w metrach wyrażoną
 zawsze liczbą naturalną. Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n metrów.
  Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n."""

# f(i) - maksymalny zysk, który można uzyskać z pocięcia i sprzedania pręta długości i

# f(0) = 0
# f(i) = max(f(i - j) + A[j]) ; 1 <= j <= i


def rod(price, n):
    profit = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            profit[i] = max(profit[i], price[j] + profit[i - j])

    return profit[n]


price = [0, 2, 2, 7, 5, 3]
print(rod(price, 5))