"""Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo word jest poprawnym słowem
 danego języka. Dostajemy na wejściu stringa bez spacji. Podaj algorytm, który stwierdzi, czy da się tak powstawiać
 spacje do wejściowego stringa, że ciąg słów który otrzymamy tworzą słowa z danego języka. Np. “alamakotainiemapsa”
 możemy zapisać jako “ala ma kota i nie ma psa”. Podaj również, jak wykorzystać algorytm, aby uzyskać przykładowe
 poprawne rozdzielenie stringa spacjami, jeśli oczywiście ono istnieje. Algorytm ma być szybki, ale najważniejsze,
 żeby był poprawny!!!."""

# f(i, j) - czy word[i:j] jest poprawny

# f(i, j) = logic_sum(f(i, k) and f(k, j)) or dict(word[i:j]) ; i < k < j


def valid(word, F, i, j):
    if F[i][j] is not None:
        return F[i][j]

    if fdict(word[i:j]):
        F[i][j] = True
        return F[i][j]

    for k in range(i + 1, j):
        if (valid(word, F, i, k) and valid(word, F, k, j)):
            F[i][j] = True
            return F[i][j]

    F[i][j] = False
    return F[i][j]


def valid_word(word):
    n = len(word)
    F = [[None] * n for _ in range(n)]

    return valid(word, F, 0, n - 1)
