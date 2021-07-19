"""Dany jest zbiór punktów X = {x1, . . . , xn} na
prostej. Prosze podac algorytm, który znajduje minimalna liczbe przedziałów jednostkowych domknietych,
potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jesli X = {0.25, 0.5, 1.6} to potrzeba dwóch
przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4])."""

# sortujemy punkty z X niemalejąco, początek przedziału kładziemy w pierwszym punkcie, który nie jest zakryty. całość
# powtarzamy aż przykryjemy wszystkie punkty


def singular_ranges_coverage(X):
    X.sort()
    cnt = 1
    i = 1
    dst = X[0] + 1
    while i < len(X):
        if X[i] - dst > 0:
            dst = X[i] + 1
            cnt += 1
        i += 1

    return cnt


X = [0.25, 0.5, 1.6, 3.2, 1.7, 2.9, 5.4, 4.3]
print(singular_ranges_coverage(X))