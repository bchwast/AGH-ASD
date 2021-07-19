from copy import deepcopy
from queue import PriorityQueue

"""Dany jest graf skierowany G = (V, E) oraz funkcja opisująca pojemności jego krawędzi c: E → N. Proszę zaimplementować 
 funkcję max extending path, która dostaje na wejściu G, c, oraz wierzchołki s i t i znajduje ścieżkę skierowaną z s do 
 t o maksymalnej przepustowości (czyli minimalna przepustowość krawędzi na ścieżce powinna być jak największa).
 Graf G oraz funkcja c reprezentowane są łącznie przez listy sąsiedztwa. Formalnie zbiorem wierzchołków jest 
 V = {0, 1, . . . , n − 1} a G[i] to lista par opisujących krawędzie wychodzące z wierzchołka i. 
 Pierwszym elementem każdej pary jest wierzchołek do którego dochodzi krawędź a drugim elementem jest pojemność tej 
 krawędzi. Przykładowo lista:
    G = [[(1,4), (2,3)],    # 0
         [(3,2)],           # 1
         [(3,5)],           # 2
         []]                # 3

 opisuje graf z wierzchołkami V = {0, 1, 2, 3}, gdzie z wierzchołka 0 mamy krawędzie do wierzchołków 1 i 2 o 
 przepustowościach 4 i 3. Z wierzchołka 1 mamy krawędź do wierzchołka 3 o przepustowości 2, a z wierzchołka 2 mamy 
 krawędź do 3 o przepustowości 5. Funkcja powinna zwracać ścieżkę jako listę jej kolejnych krawędzi. 
 Implementowana funkcja powinna być postaci:
    def max_extending_path( G, s, t )
 Dla przykładowego grafu G oraz s = 0 i t = 3 wynikiem powinna być lista [0, 2, 3]. Pojemność tej ścieżki to 3.
"""


def max_extending_path( G, s, t ):
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
    return []
  

  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")
  
