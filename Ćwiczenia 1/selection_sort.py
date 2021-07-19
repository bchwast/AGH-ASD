def selection_sort(T):
    n = len(T)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if T[j] < T[min_i]:
                min_i = j
        T[i], T[min_i] = T[min_i], T[i]


T = [4, 3, 2, 10, 12, 1, 5, 6]
selection_sort(T)
print(T)