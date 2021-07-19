def partition(T, low, high):
    pivot = T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[high] = T[high], T[i + 1]
    return i + 1


def quicksort(T, low, high):
    while low < high:
        mid = partition(T, low, high)
        if mid - low < high - mid:
            quicksort(T, low, mid - 1)
            low = mid + 1
        else:
            quicksort(T, mid + 1, high)
            high = mid - 1


def if_sums(T):
    quicksort(T, 0, len(T) - 1)

    for i in range(len(T)):
        flag = False
        dest, left, right = T[i], 0, len(T) - 1
        while left < len(T) and right > -1 and left < right:
            if left != i and right != i:
                if T[left] + T[right] < dest:
                    left += 1
                elif T[left] + T[right] > dest:
                    right -= 1
                else:
                    flag = True
                    break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1

        if not flag:
            return False

    return True

T = [2, 1, 0, 1, 0, 0]
print(if_sums(T))