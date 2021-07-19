from queue import Queue


class Vortex:
    def __init__(self, neighbours):
        self.parent = None
        self.d = -1
        self.visited = False
        self.neighbours = neighbours

    def __str__(self):
        return f"(parent: {self.parent}, d: {self.d}, visited: {self.visited}, neighbours: {self.neighbours})\n "

    def __repr__(self):
        return f"(parent: {self.parent}, d: {self.d}, visited: {self.visited}, neighbours: {self.neighbours})\n"


def graphize(G):
    graph = [Vortex(G[i]) for i in range(len(G))]
    return graph


def bfs(G, s):
    Q = Queue()
    G[s].d = 0
    G[s].visited = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u].neighbours:
            if not G[v].visited:
                G[v].visited = True
                G[v].d = G[u].d + 1
                G[v].parent = u
                Q.put(v)


G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
graph = graphize(G)
start = 0
bfs(graph, start)
print(graph)
