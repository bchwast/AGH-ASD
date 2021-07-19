# sortujemy klocki po lewych krawędziach, chcemy poscalać ze sobą klocki o równych końcach i początkach
# przechodzimy po klockach i dla każdego klocka mogącego być początkiem wyszukiwaniem binarnym szukamy klocka o początku
# równym końcowi tego pierwszego
# tworzymy tablicę początków i końców super-klocków jako tablicę trójek (współrzędna, p/k, indeks super-klocka)
# sortujemy tę tablicę niemalejąco po współrzędnych
# inicjalizujemy stos, przeglądamy tablicę, jak trafimy na początek to wrzucamy go na stos, jak trafimy na koniec to
# sprawdzamy czy należy do tego samego klocka co ostatni początek na stosie, jeżeli nie to zwracamy False
# jeżeli nie znaleźliśmy ani jednej różnej pary to dla wejściowego zbioru klocków istnieje poprawna kolejność spadania


def binary_search(K, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if K[mid][0] == x:
            return mid
        elif K[mid][0] > x:
            return binary_search(K, low, mid - 1, x)
        else:
            return binary_search(K, mid + 1, high, x)
    return False


def falling_blocks(K):
    n = len(K)
    K.sort(key=lambda x: x[0])
    glued = [False] * n
    flag = False

    for i in range(n):
        if flag:
            i -= 1
        flag = False
        if not glued[i]:
            extend = binary_search(K, 0, n - 1, K[i][1])
            if extend and glued[extend]:
                K[i] = (K[i][0], K[extend][1])
                glued[extend] = True
                flag = True

    B = []
    ind = 0
    for i in range(n):
        if not glued[i]:
            B.append((K[i][0], "p", ind))
            B.append((K[i][1], "k", ind))
            ind += 1

    stack = []
    n = len(B)
    B.sort(key=lambda x: x[0])

    for i in range(n):
        if B[i][1] == "p":
            stack.append(B[i])
        else:
            if stack[len(stack) - 1][2] != B[i][2]:
                return False
            else:
                stack.pop()

    return True


K = [(2, 4), (5, 7), (3, 6), (4, 5)]
print(falling_blocks(K))