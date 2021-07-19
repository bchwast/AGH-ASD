from queue import PriorityQueue

"""Dana jest lista zleceń. Każde zlecenie wymaga pewnego kapitału początkowego Ci, który należy mieć, żeby zacząć 
 zlecenie oraz zysk Pi, który doda się do naszego całkowitego kapitału, gdy wykonamy zlecenie. 
 Mając kapitał początkowy W i liczbę k wybierz co najwyżej k zleceń tak, że skończysz z maksymalnym możliwym kapitałem.
 Przykład: k = 2, W = 0, P=[1,2,3], C=[0,1,1]. 
 Rozwiązanie: na początku mamy kapitał 0, więc możemy wybrać tylko zlecenie pierwsze. Po jego ukończeniu mamy 
 kapitał równy 1, więc możemy wybrać albo zlecenie 2 albo 3. Zlecenie 3 ma większy profit więc wybieramy zlecenie 3, 
 ponieważ możemy wybrać już tylko 1 zlecenie (k = 2). Kończymy z kapitałem 4."""

# za każdym razem wybieramy zlecenie o największym zysku, na które wystarczy nam kapitału
# tworzymy pomocniczą tablicę zawierającą trójki (potrzebny kapitał, profit, indeks), sortujemy niemalejąco według
# potrzebnego kapitału, będziemy zapamiętywać, które zlecenia już wzięliśmy. za każdym razem bierzemy te zlecenia, na
# które nas stać i których jeszcze nie wzięliśmy, wrzucamy je do kolejki priorytetowej (-profit, indeks)
# wybieramy zlecenie o największym proficie i odznaczamy, że je wzięliśmy


def max_capital(P, C, W, k):
    n = len(P)
    Q = PriorityQueue()
    tasks = [None] * n
    taken = [False] * n
    for i in range(n):
        tasks[i] = (C[i], P[i], i)
    tasks.sort(key=lambda x: x[0])

    capital = W
    for _ in range(k):
        i = 0
        while i < n and tasks[i][0] <= capital:
            if not taken[tasks[i][2]]:
                Q.put((-1 * tasks[i][1], tasks[i][2]))
            i += 1

        p, ind = Q.get()
        capital -= p
        taken[ind] = True

    result = []
    for i in range(n):
        if taken[i]:
            result.append(i)

    return result, capital


k = 2
W = 0
P = [1, 2, 3]
C = [0, 1, 1]
print(max_capital(P, C, W, k))



