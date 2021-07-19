"""Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Prosze zaproponowac algorytm
podajacy kolejnosc wyłaczania stacji."""

# odpalamy dfs'a, każdy wierzchołek po przetworzeniu wrzucamy na stos, poprawną kolejnością usuwania jest kolejność
# odwrotna do kolejność wierzchołków względem ich czasów przetworzenia. wystarczy nam jedno wykonanie dfs'a, zatem
# złożoność wyniesie O(n + m), czyli maksymalnie O(n^2) dla grafu pełnego


def remove_vertexes(G):
    def dfs(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs(G, v)
        result.append(u)


    n = len(G)
    visited = [False] * n
    parent = [None] * n
    result = []
    for u in range(n):
        if not visited[u]:
            dfs(G, u)

    return result


G = [[1, 5], [0, 2, 4, 5], [1, 3, 4, 5], [2, 4], [3, 2, 1, 5], [0, 1, 2, 4]]
print(remove_vertexes(G))
