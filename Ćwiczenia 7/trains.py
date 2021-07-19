from queue import PriorityQueue

"""Mamy dany pewien rozkład pociągów, dany jako tablica n krotek (arrival_time, departure_time),
 przy czym są one posortowane niemalejąco według arrival_time. Chcemy wiedzieć,
 czy nasza stacja mająca m peronów jest w stanie bezkonfliktowo obsłużyć te pociągi,
 tzn. w żadnym momencie nie będzie “rywalizacji” pociągów o dostępne perony.
 Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie.
"""

# przechodzimy po pociągach pierwsze m wstawiamy do kolejki priorytetowej według departure_time, dla każdego kolejnego
# pociągu sprawdzamy czy jego arrival_time jest >= od departure_time na szczycie kolejki. jeżeli tak to usuwamy szczyt
# z kolejki i wstawiamy do niej właśnie rozpatrywany pociąg, jeżeli nie to zwracamy False. po przejściu całej listy
# możemy zwrócić True


def trains(A, m):
    n = len(A)
    Q = PriorityQueue(m)
    for i in range(m):
        Q.put(A[i][1])

    for i in range(m + 1, n):
        top = Q.get()
        if A[i][0] < top:
            return False
        else:
            Q.put(A[i][1])

    return True