# f(i) - największa możliwa wartość skradzionych przedmiotów od dla indeksów od 0 do i

# f(i) - max(f(i - 1), f(i - 2) + A[i]); i > 1
# f(0) = A[0]
# f(1) = max(A[0], A[1])


def get_solution(A, F, i):
    if i < 0:
        return []
    if i > 0 and F[i] == F[i - 1]:
        return get_solution(A, F, i - 1)
    return get_solution(A, F, i - 2) + [A[i]]


def goodThief(A):
    n = len(A)
    F = [float("-inf")] * n
    F[0] = A[0]
    if n > 1:
        F[1] = max(A[0], A[1])

    for i in range(2, n):
        F[i] = max(F[i - 1], F[i - 2] + A[i])

    res = get_solution(A, F, n - 1)
    print(res)
    return F[n - 1]


A = [1, 2, 3, 1, 1, 1, 1, 5000, 1]
print(goodThief(A))
