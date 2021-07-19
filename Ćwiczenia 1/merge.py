def merge(T, a, c, b):
    n1 = c - a + 1
    n2 = b - c
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = T[a+i]
    for j in range(n2):
        R[j] = T[c+j+1]
    L[n1] = 1000
    R[n2] = 1000
    i = j = 0
    for k in range(a, b+1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1


def mergesort(T, a, b):
    if a < b:
        c = (a+b)//2
        mergesort(T, a, c)
        mergesort(T, c+1, b)
        merge(T, a, c, b)

T = [2, 4, 5, 7, 1, 2, 3, 6]
mergesort(T, 0, len(T)-1)
print(T)