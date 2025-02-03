import networkx as nx
from data import cities, roads_with_length
from helpers import convert_graph_to_dict
from graph_search_algorithms import dijkstra_with_heap

# Створюємо граф
weighted_graph = nx.Graph()

# Додавання вершин (обласні центри України)
weighted_graph.add_nodes_from(cities)

# Додавання ребер з вагами (ваги - умовні відстані між містами у км)
weighted_graph.add_weighted_edges_from(roads_with_length)

# Конвертація графа NetworkX у словникову структуру
graph_dict = convert_graph_to_dict(weighted_graph)

start_city = "Київ"
shortest_paths = dijkstra_with_heap(graph_dict, start_city)

print(f"Найкоротші відстані від {start_city}:")
for city, distance in shortest_paths.items():
    print(f"{city}: {distance} км")