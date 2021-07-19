"""Dostając na wejściu string złożony z liter a-z, zwrócić najdłuższy jego fragment, który jest palindromem.
Palindrom to ciąg znaków, który wygląda tak samo czytany zarówno od lewej, jak i od prawej strony.
"""

# f(i, j) = {False, True} - czy string od i do j jest palindromem

# f(i, i) = True
# f(i, i + 1) = T[i] == T[i + 1]
# f(i, j) = f(i + 1, j - 1) and T[i] == T[j]

# zwracamy największe l = j - i + 1, dla którego f(i, j) == True


def palindrome(text):
    n = len(text)

    solutions = [[False] * n for _ in range(n)]

    maxl = 1
    for i in range(n):
        solutions[i][i] = True

    for i in range(n - 1):
        if text[i] == text[i + 1]:
            solutions[i][i + 1] = True
            maxl = 2

    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1

            if solutions[i + 1][j - 1] and text[i] == text[j]:
                solutions[i][j] = True

                if l > maxl:
                    maxl = l

    for i in range(n - maxl + 1):
        if solutions[i][i + maxl - 1]:
            return maxl, text[i:i+maxl]


T = "najak"
print(palindrome(T))
