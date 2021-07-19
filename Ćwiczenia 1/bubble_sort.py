def bubble_sort(T):
    n = len(T)
    for _ in range(n):
        swap = False
        for j in range(n - 1):
            if T[j + 1] < T[j]:
                T[j], T[j + 1] = T[j + 1], T[j]
                swap = True
        if not swap:
            return


T = [4, 3, 2, 10, 12, 1, 5, 6]
bubble_sort(T)
print(T)