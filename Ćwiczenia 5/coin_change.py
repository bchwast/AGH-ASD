"""Mamy dana tablice z nominałami monet stosowanych w pewnym dziwnym
kraju, oraz kwote T. Prosze podac algorytm, który oblicza minimalna ilosc monet potrzebna do wydania
kwoty T (algorytm zachłanny, wydajacy najpierw najwieksza monete, nie działa: dla monet 1, 5, 8 wyda
kwote 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)."""

# f(i) - minimalna ilość monet potrzebna do wydania kwoty i

# f(0) = 0
# f(i) = min(f(i - T[c])) + 1 ; 0 <= c < len(T)


def coin_change(coins, target):
    solutions = [float("inf")] * (target + 1)
    solutions[0] = 0

    for i in range(1, target + 1):
        for c in range(len(coins)):
            if i - coins[c] >= 0:
                result = solutions[i - coins[c]]

                if result != float("inf"):
                    solutions[i] = min(solutions[i], result + 1)

    if solutions[target] != float("inf"):
        return solutions[target]
    return -1


coins = [1, 3, 5, 7]
print(coin_change(coins, 1))