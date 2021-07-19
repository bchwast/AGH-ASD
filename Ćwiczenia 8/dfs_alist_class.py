class Vortex:
    def __init__(self, neighbours):
        self.visited = False
        self.parent = None
        self.neighbours = neighbours

    def __str__(self):
        return f"(parent: {self.parent}, visited: {self.visited}, neighbours: {self.neighbours})\n "

    def __repr__(self):
        return f"(parent: {self.parent}, visited: {self.visited}, neighbours: {self.neighbours})\n"


def graphize(G):
    graph = [Vortex(G[i]) for i in range(len(G))]
    return graph


def dfs(G):
    n = len(G)
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        time += 1
        G[u].visited = True

        for v in G[u].neighbours:
            if not G[v].visited:
                G[v].parent = u
                dfs_visit(G, v)
        time += 1

    for u in range(n):
        if not G[u].visited:
            dfs_visit(G, u)



G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
graph = graphize(G)
dfs(graph)
print(graph)