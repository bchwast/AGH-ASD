def bubble_sort(T):
    n = len(T)
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            if T[j-1] > T[j]:
                T[j], T[j-1] = T[j-1], T[j]


def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        el = T[i]
        j = i - 1
        while j >= 0 and T[j] > el:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = el


def selection_sort(T):
    n = len(T)
    for i in range(n-1):
        smol = i
        for j in range(i+1, n):
            if T[j] < T[smol]:
                smol = j
        T[i], T[smol] = T[smol], T[i]


T = [6, 23, 7, 3, 7, 23, 74, 545, 5]
#bubble_sort(T)
#insertion_sort(T)
selection_sort(T)
print(T)