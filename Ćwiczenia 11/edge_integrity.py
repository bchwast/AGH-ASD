"""Dany jest graf nieskierowany G = (V,E). Mówimy, ze spójnosc
krawedziowa G wynosi k jesli usuniecie pewnych k krawedzi powoduje, ze G jest niespójny, ale usuniecie
dowolnych k − 1 krawedzi nie rozspójnia go. Prosze podac algorytm, który oblicza spójnosc krawedziowa danego grafu."""

# wybieramy dowolny wierzchołek będący źródłem, szukamy minmalnego maksymalnego przepływu, gdzie ujściem będzie każdy
# z pozostałych wierzchołków