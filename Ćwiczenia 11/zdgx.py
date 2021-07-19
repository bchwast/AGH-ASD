print("Cwiczenia 13 i ostatnie :)")


# zadanie obowiązkowe poprzednik/następnik
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def insert(node, key):
    if node.key > key:
        if node.left is None:
            node.left = BSTNode(key)
            node.left.parent = node
        else:
            insert(node.left, key)
    else:
        if node.right is None:
            node.right = BSTNode(key)
            node.right.parent = node
        else:
            insert(node.right, key)


def find(node, key):
    if node.key == key:
        return node
    elif node.key < key:
        if node.right is not None:
            return find(node.right, key)
        else:
            return None
    else:
        if node.left is not None:
            return find(node.left, key)
        else:
            return None


def tree_max(node):
    while node.right is not None:
        node = node.right
    return node


def tree_min(node):
    while node.left is not None:
        node = node.left
    return node


# operacja poprzednika, operacja następnika
def predecessor(node):
    if node.left is not None:
        return tree_max(node.left)
    while node.parent is not None:
        if node.parent.right == node:
            return node.parent
        node = node.parent
    return None


def successor(node):
    if node.right is not None:
        return tree_min(node.right)
    while node.parent is not None:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None


# koniec zadania obowiązkowego poprzednik/następnik


# zadanie obowiazkowe - wiele zrodel i ujsc


# implementacje kolejki wklejam juz wczesniej przygotowana
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):  # O(1)
        return not self.head

    def put(self, data):  # O(1)
        node = Node(data, None)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get(self):  # O(1)
        data = self.head.data
        self.head = self.head.next
        if self.is_empty():  # zabezpieczenie
            self.tail = None
        return data


# reprezentacja : macierz sąsiedztwa grafu
class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.length = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * self.length

        Q = Queue()
        Q.put(s)

        visited[s] = True
        parent[s] = None

        while not Q.is_empty():
            u = Q.get()
            for i in range(self.length):
                if not visited[i] and self.graph[u][i] > 0:
                    Q.put(i)
                    visited[i] = True
                    parent[i] = u

        return visited[t]

    def edmonds_karp(self, source, sink):

        parent = [None] * self.length
        max_flow = 0

        # zwiększa przeplyw kiedy istnieje kolejna sciezka z zrodla do ujscia
        while self.BFS(source, sink, parent):

            # znajduje max flow na znalezionej sciezce
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # sumuje wszystkie znalezione przepływy
            max_flow += path_flow

            # odejmuje max flow danej sciezki od kazdej krawedzi
            # i dodaje to do jego odwróconej
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def multi_max_flow(c, array_s, array_t):
    main_s = len(c)
    for col in c:
        col.append(0)
    c.append([0 for _ in range(len(c) + 1)])
    for s in array_s:
        c[main_s][s[0]] = s[1]

    main_t = len(c)
    for col in c:
        col.append(0)
    c.append([0 for _ in range(len(c) + 1)])
    for t in array_t:
        c[t[0]][main_t] = t[1]

    G = Graph(c)
    return G.edmonds_karp(main_s, main_t)


c = [[0 for j in range(5)] for i in range(5)]
c[0][2] = 2
c[0][3] = 3
c[1][2] = 2
c[1][4] = 3
s = [(0, 4), (1, 3)]
t = [(2, 3), (3, 1), (4, 3)]

# algorytm o zlozonosci O(VE^2)
print(multi_max_flow(c, s, t))


# zadanie obowiazkowe - wiele zrodel i ujsc


# wyznaczanie ktorym co do wielkosci w drzewie jest zadany wezel

class BSTNode:
    def __init__(self, key, elems):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.elems = elems


def elems(node):
    count = 1
    visited = False
    while node.parent != None:
        if node.left != None and not visited:
            count += node.left.elems
        if node.parent.left == node:
            visited = True
        else:
            visited = False

        node = node.parent

    if node.left != None and not visited:
        count += node.left.elems

    return count

# koniec


class graph:

    def __init__(self, size):
        self.m = [[0] * size for i in range(size)]
        self.size = size
        self.edges = 0

    def add_edge(self, v, u, weight):
        self.m[v][u] = weight
        self.m[u][v] = weight
        self.edges += 1

    def printG(self):
        for i in g.m:
            print(i)


from collections import deque


def BFS(g, s, t, parents):
    q = deque()
    number = len(g)

    visited = [False] * number
    q.appendleft(s)
    visited[s] = True

    while len(q) != 0:
        u = q.pop()

        for i in range(number):
            if len(q) == 0: q = deque()
            if g[u][i] != 0 and visited[i] == False:
                parents[i] = u
                visited[i] = True
                q.appendleft(i)

    return visited[t]


# maksymalny przepływ z wierzchołka s do t
def Ford_Fulkerson(g, s, t):
    parents = [None] * len(g)
    flow = 0

    while BFS(g, s, t, parents):

        current = t
        cur_flow = float("inf")

        while current != s:
            if g[parents[current]][current] < cur_flow:
                cur_flow = g[parents[current]][current]
            current = parents[current]

        flow += cur_flow
        v = t

        while v != s:
            g[parents[v]][v] -= cur_flow
            g[v][parents[v]] += cur_flow
            v = parents[v]
    return flow


def flow(g, s, t):
    matrix = [[0] * (g.size + g.edges) for _ in range(g.size + g.edges)]

    current = g.size
    for i in range(g.size):
        for j in range(g.size):
            if i < j and g.m[i][j] != 0:
                matrix[i][j] = g.m[i][j]
                matrix[j][current] = matrix[current][i] = g.m[i][j]
                current += 1

    return Ford_Fulkerson(matrix, s, t)

g = graph(6)
g.add_edge(0,1,4)
g.add_edge(0,3,8)
g.add_edge(1,2,5)
g.add_edge(1,3,7)
g.add_edge(2,3,6)
g.add_edge(2,5,7)
g.add_edge(3,4,10)
g.add_edge(4,5,6)

print(flow(g,0,5))