from queue import PriorityQueue


# klasa Node do stworzenia drzewa
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.ind = None
        self.left = None
        self.right = None

    def __gt__(self, other):
        return self.freq > other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq


# funkcja tworząca kody
def c_code(T, node, code):
    # jak dotarliśmy do liścia to możemy odczytać kod i zapisać do tablicy
    if node.ind != None:
        T[node.ind] = code

    # idziemy do lewego poddrzewa i dodajemy 1 do kodu
    if node.left is not None:
        c_code(T, node.left, code + "1")

        # idziemy do prawego poddrzewa i dodajemy 0 do kodu
        if node.right is not None:
            c_code(T, node.right, code + "0")


# właściwa funkcja
def huffman(S, F):
    n = len(S)
    # tworzymhy tablicę dla kodów
    T = [None] * n
    # inicjalizujemu kolejkę
    huff = PriorityQueue(n)

    # dla każdego symbolu tworzymy liść i dodajemy go do kolejki
    for i in range(n):
        a = Node(F[i])
        a.ind = i
        huff.put(a)

    # działamy do momentu aż w kolejce zostanie jeden element
    while huff.qsize() > 1:
        # zdejmujemy z kolejki dwa elementy o najniższej częstotliwości
        a = huff.get()
        b = huff.get()
        # tworzymy node odsyłającego do tamtych dwóch elementów
        root = Node(a.freq + b.freq)
        root.left = a
        root.right = b
        # do kolejki dodajemy nowego node'a z częstotliwością będącą sumą częstotliwości dwóch poprzednio zdjętych
        huff.put(root)

    # tworzymy kody
    if n > 1:
        c_code(T, root, "")
    elif n == 1:
        T[0] = "0"

    # zliczamy łączną liczbę bitów potrzebną do wypisania napisu i wypisujemy symbole wraz z kodami
    cost = 0
    for i in range(n):
        print(f"{S[i]} : {T[i]}")
        cost += F[i] * len(T[i])
    # wypisujemy koszt wypisania napisu
    print(f"dlugosc napisu: {cost}")


S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']
F = [27, 32, 123, 15, 4, 32, 23, 13, 44, 32, 12, 5, 3, 145, 54, 34, 98, 102, 76, 243, 45, 65, 78]

huffman(S, F)

