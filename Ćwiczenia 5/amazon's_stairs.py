"""Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. początkowo stoimy na pozycji 0,
 wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.

Przykład A = {1,3,2,1,0}
Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4. Należy policzyć na ile sposobów mogę
przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
"""

# f(i) - na ile sposobów mogę przejść z pozycji 0 na pozycję i

# f(0) = 1
# f(i) = sum(f(i - k)); 1 <= k <= i; jeżeli przejście jest możliwe


def amazon(T):
    n = len(T)
    F = [0] * n
    F[0] = 1

    for i in range(n):
        for j in range(1, min(T[i] + 1, n - i)):
            F[i + j] += F[i]

    return F[n - 1]


T = [2, 1, 3, 2, 1, 0]
print(amazon(T))