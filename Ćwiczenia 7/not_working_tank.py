from queue import PriorityQueue


def tank(S, P, L, t):

    t_pos = len(S)
    S.append(t)
    P.append(0)

    total_cost = 0
    fuel = L - S[0]

    PQ = PriorityQueue()

    i = 0
    j = 1
    while i != t_pos:

        while j < len(S) and S[i] + L >= S[j]:
            PQ.put((P[j], S[j]))
            j += 1

        cheapest = (0, 0)
        while cheapest[1] <= S[i]:
            cheapest = PQ.get()
        PQ.put(cheapest)

        #print(i, j, '->', cheapest)

        if cheapest[0] < P[i]:
            k = i + 1
            while P[k] > P[i]:
                k += 1

            refuel = S[k] - S[i] - fuel
            fuel = 0
            i = k
            total_cost += refuel * P[i]
            #print("ONE", refuel)
        else:
            refuel = L - fuel
            fuel = L - (S[i+1] - S[i])
            total_cost += refuel * P[i]
            i += 1
            #print("TWO", refuel)

        #print("cost =", total_cost)

    return total_cost


L = 10
S = [8, 11, 15, 16]
P = [40, 7, 15, 12]
t = 23

print(tank(S, P, L, t))