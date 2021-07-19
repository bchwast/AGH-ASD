"""W Krakowie w godzinach szczytu są korki, dlatego kierowcom bardziej zależy na czasie niż na realnej odległości
 między dwoma punktami. Mamy mapę Krakowa, między skrzyżowaniami na ulicach są zaznaczone odległości i czasy przejazdu.
 W Krakowie (jak wszyscy wiemy ;) ) są ulice jedno- i dwukierunkowe. Kierowcy potrzebują aplikacji, która pomoże im
 znajdować drogi, które pozwalają dotrzeć ze skrzyżowania A do B w jak najkrótszym czasie, a spośród tych o
 najmniejszym czasie wybiera i zwraca najkrótszą pod względem odległości.
 Mamy przetworzyć Q zapytań w postaci (skrzyżowanieA, skrzyżowanieB) i na każde z nich odpowiedzieć parą (czas, dystans)
 najlepszej drogi. Wszystkie zapytania odnoszą się do tego samego grafu.
 Jakie rozwiązanie daje najlepszą klasę złożoności w każdym z poniższych przypadków?
 1) Q = O(1), E = O(V)
 2) Q = O(1), E = O(V^2)
 3) Q = O(V), E = O(V)
 4) Q = O(V), E = O(V^2) """

 # Dla 1) i 3) najlepiej jest użyć implementacji algorytmu Dijkstry na kolejce priorytetowej, gdzie poza informacją
 # o wadze, wrzucamy do kolejki również informację o odległości i w razie równości tej pierwszej dokonujemy relaksacji
 # na podstawie tej drugiej
 # Dla 2) używamy implementacji algorytmu Dijkstry na tablicy
 # Dla 4) możemy użyć implementacji algorytmu Dijkstry na tablicy lub algorytmu Floyda-Warshalla