"""Cersei i Jaime mają 3 - letniego syna. Przygotowali listę N aktywności podanych jako pary,
 reprezentujące czas rozpoczęcia i zakończenia danej aktywności.
 Zaimplementuj algorytm, który przyporządkuje każdej aktywności literę C lub J, oznaczającą,
 że daną aktywność z synem wykona odpowiednio Cersei lub Jaime, w taki sposób,
 że żaden rodzic nie wykonuje pokrywających się czasowo aktywności.
 Jeżeli takie przyporządkowanie nie istnieje, to algorytm zwraca “IMPOSSIBLE”, a jeśli istnieje, to zwraca odpowiedniego stringa.
 Przykładowo: (99, 150), (1, 100), (100, 301), (2,5), (150, 250) - odpowiedź to JCCJJ (lub CJJCC).
"""

# tworzymy trójki (czas, p/k, i) informujące nas o tym czy dany punkt czasu jest początkiem, czy końcem przedziału oraz
# z którego przedziału pochodzi.
# sortujemy te trójki niemalejąco, przechodzimy od początku i jeżeli rozpoczniemy trzeci przedział nie kończąc wcześniej
# żadnego z poprzednich to oznacza, że nie jesteśmy w stanie podzielić aktywności na dwójkę rodziców


def child_care(A):
    n = len(A)
    T = [None] * (2 * n)
    for i in range(n):
        T[2 * i] = (A[i][0], "p", i)
        T[(2 * i) + 1] = (A[i][1], "k", i)
    T.sort()
    result = [None] * n
    curr = [(0, -1), (0, -1)]

    for i in range(2 * n):
        if T[i][1] == "p":
            if curr[0][0] == curr[1][0] == 1:
                return "IMPOSSIBLE"
            elif curr[0][0] == 0:
                result[T[i][2]] = "J"
                curr[0] = (1, T[i][2])
            else:
                result[T[i][2]] = "C"
                curr[1] = (1, T[i][2])
        else:
            if curr[0][1] == T[i][2]:
                curr[0] = (0, -1)
            else:
                curr[1] = (0, -1)

    res = ""
    for i in range(n):
        res += result[i]
    return res


A = [(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]
print(child_care(A))
