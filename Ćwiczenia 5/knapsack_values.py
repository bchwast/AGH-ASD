def knapsack_values(P, W, MaxW):
    result = [-1] * (sum(P) + 1)
    result[0] = 0

    for i in range(len(P)):
        for j in range(len(result) - 1, -1, -1):
            if result[j] >= 0:
                if result[j + P[i]] == -1:
                    result[j + P[i]] = result[j] + W[i]
                else:
                    result[j + P[i]] = min(result[j + P[i]], result[j] + W[i])

    profit = len(result) - 1
    while profit >= 0:
        if -1 < result[profit] <= MaxW:
            return profit
        profit -= 1

    return profit

P = [21, 3, 6, 3, 87, 34, 7, 34, 97, 34]
W = [4, 5, 12, 9, 1, 13, 2, 5, 2, 5]
MaxW = 30

print(knapsack_values(P, W, MaxW))
