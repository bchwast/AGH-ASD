def insertion_sort(T):
    n = len(T)
    for i in range(n):
        curr_i = i
        for j in range(i):
            if T[curr_i] < T[j]:
                T[curr_i], T[j] = T[j], T[curr_i]


T = [4, 3, 2, 10, 12, 1, 5, 6]
insertion_sort(T)
print(T)
