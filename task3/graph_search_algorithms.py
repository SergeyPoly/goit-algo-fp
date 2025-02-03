import heapq

def dijkstra_with_heap(graph, start):
    """
    Алгоритм Дейкстри для пошуку найкоротших шляхів у зваженому графі з використанням бінарної купи.
    :param graph: Зважений граф у вигляді словника {вузол: {сусід: вага}}.
    :param start: Початкова вершина.
    :return: Найкоротші відстані від початкової вершини до всіх інших вершин.
    """
    # Ініціалізуємо словник для зберігання найкоротших відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Відстань до початкової вершини = 0

    # Черга (heap), яка містить вершини та їхні поточні відстані
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більша за поточну, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдений коротший шлях до сусіда, оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Додаємо сусіда до черги з оновленою відстанню
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances