def targetSum(T, target):
    i = 0
    j = len(T) - 1
    while i <= j:
        while i <= j and T[i] + T[j] <= target:
            if T[i] + T[j] == target:
                return True
            i += 1
        j -= 1

    return False


T = [1,3,3,5,6,7,9,9,10,12]
print(targetSum(T, 16))