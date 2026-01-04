import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_colors(count):
    colors = []
    for i in range(count):
        level = int(30 + (200 * (i / count)))
        colors.append(f'#{level:02X}{level:02X}F0')
    return colors

def bfs_visualize(root):
    if not root: return
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    
    colors = generate_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]
    draw_tree(root, "BFS Traversal")

def dfs_visualize(root):
    if not root: return
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    
    colors = generate_colors(len(visited))
    for i, node in enumerate(visited):
        node.color = colors[i]
    draw_tree(root, "DFS Traversal")

def build_heap(data, index=0):
    if index >= len(data): return None
    node = Node(data[index])
    node.left = build_heap(data, 2 * index + 1)
    node.right = build_heap(data, 2 * index + 2)
    return node

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50, 60, 70]
    
    bfs_root = build_heap(data)
    bfs_visualize(bfs_root)
    
    dfs_root = build_heap(data)
    dfs_visualize(dfs_root)