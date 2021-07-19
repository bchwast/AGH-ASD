"""W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludność przed koronawirusem.
 Prowincję można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] = 1 oznacza, że w mieście i można zbudować maszynę,
 a wartość 0, że nie można. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i,
 to miasta o indeksach j takich, że abs(i-j) < k są przez nią chronione. Należy zaproponować algorytm, który stwierdzi
 ile minimalnie maszyn potrzeba aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe."""

# stawiamy maszynę w najdalszym możliwym punkcie tak, żeby chroniła wszystkie prowincje znajdujące się przed nią.
# skaczemy o 2k - 1 i cofamy się aż znajdziemy prowincję, w której możemy postawić maszynę, jeżeli wrócimy na miejsce,
# z którego skoczyliśmy to już wiemy, że nie da się zapewnić ochrony w każdym mieście


def covid_safety(arr, k):
    n = len(arr)
    i = min(k, n - 1)
    j = -1
    cnt = 0
    while i < n:
        if i == j:
            return -1
        if arr[i] == 1:
            cnt += 1
            if i + k >= n:
                return cnt
            j = i
            i = min(2 * k + i, n)
        i -= 1
    return cnt


arr = [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
print(covid_safety(arr, 3))