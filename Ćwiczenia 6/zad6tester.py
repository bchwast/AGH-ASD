"""
Zakładam że funkcja bitonicTSP(C) jest w pliku zad6.py
i wypisuje dane w formacie:
nazwamiasta, nazwamiasta, nazwamiasta ...
łączna odległość

jak ktoś ma inaczej to może zmienić funkcję u siebie albo tutaj pogrzebać w kodzie
"""

# liczba testów i długość listy testowej
CITIES_COUNT = 50
TESTS = 100


from bitonic_tsp_result import bitonicTSP, get_path, distance
from math import *
from random import sample, randint
import io
from contextlib import redirect_stdout


def validate(output, C):
    def dist(cityA, cityB):
        return sqrt(pow(cityA[1] - cityB[1], 2) + pow(cityA[2] - cityB[2], 2))

    C.sort(key=lambda x: x[0])
    lines = output.split(sep='\n')
    order = lines[0].split(sep=',')
    your_result = float(lines[1])
    for i in range(len(order)):
        order[i] = order[i].strip()
    order = list(map(int, order))
    total = 0
    for i in range(len(order)-1):
        total += dist(C[order[i]], C[order[i+1]])

    if abs(total - your_result) <= 10e-7:
        return True
    else:
        return False


if __name__ == "__main__":
    correct = 0
    wrong = 0
    for i in range(TESTS):
        print(f"Test #{i}:")
        C = list(zip([i for i in range(CITIES_COUNT)], sample(range(CITIES_COUNT ** 2), CITIES_COUNT),
                     [randint(-CITIES_COUNT ** 2, CITIES_COUNT ** 2) for _ in range(CITIES_COUNT)]))
        C.sort(key=lambda x: x[1])
        print(C)

        output = None
        with io.StringIO() as buf, redirect_stdout(buf):
            bitonicTSP(C)
            output = buf.getvalue()

        if validate(output, C):
            correct += 1
            print("Nice.")
        else:
            wrong += 1
            print("Wrong")
    print()
    print(f"Correct tests: {correct}")
    print(f"Wrong tests: {wrong}")
