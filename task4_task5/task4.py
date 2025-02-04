from code_example import draw_tree, Node

def build_tree_from_heap(heap):
    if not heap:
        return None

    def build_node(index):
        if index >= len(heap):
            return None
        node = Node(heap[index])
        node.left = build_node(2 * index + 1)
        node.right = build_node(2 * index + 2)
        return node

    return build_node(0)


# Приклад використання:
heap = [10, 20, 15, 30, 40, 50, 100]

# Побудова дерева з купи
heap_tree_root = build_tree_from_heap(heap)

# Візуалізація дерева
draw_tree(heap_tree_root, "Візуалізація бінарної купи")
