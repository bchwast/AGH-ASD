def sum_of_two_elements(A, x):
    n = len(A)
    A.sort()
    i = 0
    j = n - 1
    while i < j:
        if A[i] + A[j] == x:
            return True
        elif A[i] + A[j] < x:
            i += 1
        else:
            j -= 1
    return False


A = [4, 2, 3, 6, 2, 8, 3, 65, 32, 6]
print(sum_of_two_elements(A, 4))