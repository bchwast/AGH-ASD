def partition(T, a, b):
    pivot = T[b]
    i = a - 1
    for j in range(a, b):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[b] = T[b], T[i + 1]
    return i + 1


def quicksort(T):
    stack = []
    stack.append((0, len(T) - 1))

    while len(stack) > 0:
        a, b = stack.pop()
        if a < b:
            c = partition(T, a, b)
            if b - a < c - b:
                stack.append((c + 1, b))
                stack.append((a, c - 1))
            else:
                stack.append((c + 1, b))
                stack.append((a, c - 1))








T = [5,7,34,7,347,2,1,-325,-523,5235,-6,2342,6]
quicksort(T)
print(T)