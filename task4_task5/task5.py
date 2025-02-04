import matplotlib.colors as mcolors
from collections import deque
from code_example import draw_tree, Node

def generate_colors(n):
    return list(mcolors.LinearSegmentedColormap.from_list("grad", ["#4B0082", "#00FFFF"])(i/n) for i in range(n))

def bfs_traversal(root):
    if not root:
        return
    queue = deque([root])
    colors = generate_colors(10)
    index = 0
    while queue:
        node = queue.popleft()
        node.color = colors[min(index, len(colors) - 1)]
        index += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    draw_tree(root, "Обхід у ширину (BFS)")

def dfs_traversal(root):
    if not root:
        return
    stack = [root]
    colors = generate_colors(10)
    index = 0
    while stack:
        node = stack.pop()
        node.color = colors[min(index, len(colors) - 1)]
        index += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    draw_tree(root, "Обхід у глибину (DFS)")

# Створення дерева
root = Node(10, "#4B0082")
root.left = Node(6, "#4B0082")
root.right = Node(15, "#4B0082")
root.left.left = Node(3, "#4B0082")
root.left.right = Node(8, "#4B0082")
root.right.left = Node(12, "#4B0082")
root.right.right = Node(18, "#4B0082")

# Візуалізація обходів
bfs_traversal(root)
dfs_traversal(root)
