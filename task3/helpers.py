# Перетворення графа NetworkX у словникову структуру для роботи з алгоритмом
def convert_graph_to_dict(weighted_graph):
    graph_dict = {node: {} for node in weighted_graph.nodes()}
    for u, v, data in weighted_graph.edges(data=True):
        graph_dict[u][v] = data['weight']
        graph_dict[v][u] = data['weight']
    return graph_dict
