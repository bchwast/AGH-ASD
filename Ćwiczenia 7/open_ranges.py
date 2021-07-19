"""Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór tego zbioru, taki że:
 1) jego rozmiar wynosi dokładnie k
 2) przedziały są rozłączne
 3) różnica między najwcześniejszym początkiem, a najdalszym końcem jest minimalna.
 Jeśli rozwiązanie nie istnieje, to algorytm powinien to stwierdzić. Algorytm powinien być w miarę możliwości szybki,
 ale przede wszystkim poprawny.
"""

# Sortujemy przedziały po początkach, dla każdego przedziału znajdujemy wyszukiwaniem binarny pierwszy taki przedział,
# który zaczyna się po nim, dalej przechodzimy po tak połączonych przedziałach, sprawdzamy czy da się w taki sposób
# przejść k przedziałów, jeżeli tak to szukamy takiego "spaceru", w którym różnica między końcem a początkiem jest
# najmniejsza


def get_index(T, low, high, value):
    if 1 < high - low:
        mid = (low + high) // 2
        if T[mid][0] > value:
            return get_index(T, low, mid, value)
        else:
            return get_index(T, mid , high, value)
    return high


def open_ranges(T, k):
    n = len(T)
    T.sort(key=lambda x: x[0])
    result = [None] * k
    l_m = float("inf")

    ind = 0
    while ind < n - k:
        curr = [T[ind]]
        i = ind
        for _ in range(1, k):
            if T[i][1] >= T[n - 1][0]:
                break
            else:
                beg = get_index(T, i + 1, n - 1, T[i][1])
                curr.append(T[beg])
                i = beg
        if len(curr) == k:
            l = curr[k - 1][1] - curr[0][0]
            if l < l_m:
                l_m = l
                for i in range(k):
                    result[i] = curr[i]
        ind += 1

    if result[0] is None:
        return None
    return result


T = [(0, 3), (4, 10), (5, 6), (11, 12)]
print(open_ranges(T, 2))

