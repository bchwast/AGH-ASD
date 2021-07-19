"""Alicja chce zorganizować przyjęcie i zastanawia się, kogo zaprosić spośród n znajomych. Stworzyła już listę par
 osób które się znają. Chce wybrać możliwie jak najwięcej osób, tak aby spełnione były dwa warunki: na przyjęciu każda
 osoba powinna znać co najmniej 5 osób oraz co najmniej 5 osób nie znać.
 Zaproponuj algorytm który przyjmuje na wejściu listę n osób oraz listę par osób które się znają, a na wyjściu daje
 możliwie najdłuższą listę gości.
"""

# tworzymy listę list znajomych osoby o indeksie i, pamiętamy ilu znajomych ma dana osoba oraz czy jest zaproszona,
# początkowo wszystkie osoby są zaproszone
# przechodzimy po liście i dla każdej osoby sprawdzamy czy zna więcej niż 5 i nie zna mniej niż 5 osób zaproszonych.
# jeżeli nie spełnia tych warunków to zaznaczamy, że ta osoba nie jest zaproszona i jej znajomym zmniejszamy licznik o 1


def guests(people, pairs):
    n = len(people)
    if n < 11:
        return None

    A = [[] for _ in range(n)]
    invited = [True] * n
    cnt = [0] * n

    for pair in pairs:
        A[pair[0]].append(pair[1])
        cnt[pair[0]] += 1
        A[pair[1]].append(pair[0])
        cnt[pair[1]] += 1

    inv = n
    for i in range(n):
        if invited[i]:
            if 5 <= cnt[i] <= inv - 5:
                continue
            else:
                invited[i] = False
                for j in A[i]:
                    cnt[j] -= 1
                inv -= 1

    res = []
    for i in range(n):
        if invited[i]:
            res.append(i)
    return res
