import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])  # Queue of (vertex, path) tuples

        while queue:
            vertex, path = queue.popleft()
            if vertex == end:
                return path

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph.neighbors(vertex):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None  # No path found

    def visualize(self, path=None):
        plt.figure(figsize=(12, 8))  # Set the size of the figure

        # Use the shell layout to better visualize small or structured networks
        shell_layout = nx.shell_layout(self.graph)

        # Draw nodes with shell layout
        nx.draw_networkx_nodes(self.graph, shell_layout, node_color='skyblue', node_size=700)

        # Highlight nodes in the path
        if path:
            nx.draw_networkx_nodes(self.graph, shell_layout, nodelist=path, node_color='lime', node_size=700)

        # Draw edges
        nx.draw_networkx_edges(self.graph, shell_layout, edge_color='black')

        # Draw node labels
        nx.draw_networkx_labels(self.graph, shell_layout, font_size=20, font_family="sans-serif")

        # Set margins to prevent cut-off
        plt.margins(0.1)

        # Show plot
        plt.show()

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

start_node = 0
end_node = 5
path = g.shortest_path(start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {path}")

# Visualize the graph
g.visualize(path=path)
