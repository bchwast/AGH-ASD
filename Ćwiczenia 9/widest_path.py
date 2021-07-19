from queue import PriorityQueue

"""Przewodnik chce przewiezc grupe K turystów z
miasta A do miasta B. Po drodze jest jednak wiele innych miast i miedzy róznymi miastami jezdza autobusy o
róznej pojemnosci. Mamy dana liste trójek postaci (x, y, c), gdzie x i y to miasta miedzy którymi bezposrednio
jezdzi autobus o pojemnosci c pasazerów.
Przewodnik musi wyznaczyc wspólna trase dla wszystkich tursytów i musi ich podzielic na grupki tak,
zeby kazda grupka mogła przebyc trase bez rodzielania sie. Prosze podac algorytm, który oblicza na ile
(najmniej) grupek przewodnik musi podzielic turystów (i jaka trasa powinni sie poruszac), zeby wszyscy
dostali sie z A do B."""

# modyfikujemy algorytm Dijkstry w taki sposób, że nie pamiętamy już jakie wierzchołki są w kolejce oraz zmieniamy
# kryterium relaksacji. w tablicy d przechowujemy informację o szerokości najszerszej ścieżki jaką możemy się dostać
# do danego wierzchołka, jeżeli możemy dostać się do wierzchołka szerszą ścieżką to aktualizujemy wartość w tablicy
# d jako minimum z szerokości ścieżki do poprzedniego wierzchołka i krawędzi łączącej go z badanym


def widest_path(G, s, t):
    def relax(u, v, weight):
        if d[v] < min(d[u], weight):
            d[v] = min(d[u], weight)
            parent[v] = u
            return True
        return False

    def path(u):
        if parent[u] is None:
            return [u]
        return path(parent[u]) + [u]

    n = len(G)
    d = [float("-inf")] * n
    parent = [None] * n
    Q = PriorityQueue()

    d[s] = float("inf")
    Q.put((d[s], s))
    while not Q.empty():
        u = Q.get()[1]
        for v in G[u]:
            if relax(u, v[0], v[1]):
                Q.put((d[v[0]], v[0]))

    route = path(t)
    # print(d)
    return route


G = [[(1, 1), (3, 2)],
     [(2, 3)],
     [],
     [(2, 5)]]
print(widest_path(G, 0, 2))