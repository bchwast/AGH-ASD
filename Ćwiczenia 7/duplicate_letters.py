"""Dany jest string, w którym niektóre litery się powtarzają. Należy zaproponować algorytm, który usunie ze stringa
 duplikaty tak, że otrzymany string będzie leksykograficznie najmniejszy.
 Przykład: cbacdcbc, odpowiedzią jest acdb.

 Wskazówka:
 ord(“a”) = 97; ord(“b”) = 98; ... ; ord(“z”) = 122
"""

# zliczamy wystąpienia poszczególnych liter, tworzymy stos, przechodzimy po stringu, dla każdej litery:
# 1) - zmniejszamy jej licznik wystąpień
# 2) - jeżeli stos jest pusty to umieszczamy ją na stosie
# 3) - jeżeli stos nie jest pusty, ale spradzana litera już na nim się znajduje to idziemy dalej
# 4) - jeżeli stos nie jest pusty to jeżeli szczyt stosu jest większy od sprawdzanej litery i jego licznik nie jest 0
#      to  usuwamy go ze stosu i patrzymy dalej
# 5) - jeżeli szczyt stosu ma licznik 0 lub jest mniejszy od sprawdzanej litery to umieszczamy ją na stosie


def duplicate_letters(string):
    n = len(string)
    letters = [0] * 26
    for i in range(n):
        letters[ord(string[i]) - 97] += 1

    in_stack = [False] * 26
    stack = []

    for i in range(n):
        letters[ord(string[i]) - 97] -= 1
        if stack == []:
            stack.append(string[i])
            in_stack[ord(string[i]) - 97] = True
        elif in_stack[ord(string[i]) - 97]:
            continue
        else:
            while stack != [] and stack[len(stack) - 1] > string[i] and letters[ord(stack[len(stack) - 1]) - 97] > 0:
                in_stack[ord(stack[len(stack) - 1]) - 97] = False
                stack.pop()
            stack.append(string[i])
            in_stack[ord(string[i]) - 97] = True

    result = ""
    for let in stack:
        result += let
    return result


print(duplicate_letters("cbacdcbcd"))