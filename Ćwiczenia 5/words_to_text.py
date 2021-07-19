"""Dana jest tablica string S[n] będąca zbiorem słów oraz ciąg znaków string t. Napisz funkcję, która
znajdzie najmniejszy taki ciąg słów ze zbioru S, aby po ich złączeniu otrzymać tekst t"""

# f(i, j) - długość najmniejszego ciągu spośród i pierwszych słów ze zbioru S, takiego, że tworzy tekst składający się
#           z j pierwszych liter tekstu t

# f(0, j) = 0
# f(i, j) = min(f(i - k, j - S[k])) + 1 ;  1 <= k <= i ; jeżeli utworzenie stringa jest możliwe


def construct_text(words, text):
    solutions = [[["", None] for _ in range(len(text) + 1)] for _ in range(len(words))]

    for i in range(1, len(text) + 1):
        for w in range(len(words)):
            if words[w] == text[:i]:
                solutions[w][i][0] = words[w]
                solutions[w][i][1] = 1
            elif w > 0 and i - len(words[w]) > 0 and solutions[w - 1][i - len(words[w])][0] + words[w] == text[:i]:
                if solutions[w - 1][i][1] != None and solutions[w - 1][i][1] < solutions[w - 1][i - len(words[w])][1] + 1:
                    solutions[w][i] = solutions[w - 1][i]
                else:
                    solutions[w][i][0] = text[:i]
                    solutions[w][i][1] = solutions[w - 1][i - len(words[w])][1] + 1
            elif w > 0:
                solutions[w][i] = solutions[w - 1][i]

    if solutions[len(words) - 1][len(text)][1] != None:
        return solutions[len(words) - 1][len(text)][1]
    return -1



text = "kajak"
words = ["ka", "ra", "jak"]
print(construct_text(words, text))