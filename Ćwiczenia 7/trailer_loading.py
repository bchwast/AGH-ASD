"""Mamy przyczepe o pojemnosci K kilogramów oraz zbiór ładunków
o wagach w1, . . . ,wn. Waga kazdego z ładunków jest potega dwójki (czyli, na przykład, dla siedmiu ładunków
wagi moga wynosic 2, 2, 4, 8, 1, 8, 16, a pojemnosc przyczepy K = 27). Prosze podac algorytm zachłanny (i
uzasadnic jego poprawnosc), który wybiera ładunki tak, ze przyczepa jest mozliwie maksymalnie zapełniona
(ale bez przekraczania pojemnosci) i jednoczesnie uzylismy mozliwie jak najmniej ładunków. (Ale jesli da sie
np. załadowac przyczepe do pełna uzywajac 100 ładunków, albo zaladowac do pojemnosci K − 1 uzywajac
jednego ładunku, to lepsze jest to pierwsze rozwiazanie)."""

# za każdym razem bierzemy najcięższy przedmiot, który jesteśmy w stanie wziąć, ponieważ wybierając mniejsze ładunki
# możemy albo wybrać sumarycznie ładunek o mniejszej masie niż masa najcięższego przedmiotu, albo po drodze z mniejszych
# ładunków uzbierać ładunek dokładnie o masie najcięższego przedmiotu


def trailer_loading(W, K):
    n = len(W)
    W.sort(reverse=True)
    result = []
    for i in range(n):
        if W[i] <= K:
            result.append(W[i])
            K -= W[i]
    return result


W = [2, 2, 4, 8, 1, 8, 16]
K = 27
print(trailer_loading(W, K))