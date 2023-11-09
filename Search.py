import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph.neighbors(start):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend([n for n in self.graph.neighbors(vertex) if n not in visited])

    def visualize(self):
        plt.figure(figsize=(12, 8))  # Set the size of the figure

        # Use the shell layout to better visualize small or structured networks
        shell_layout = nx.shell_layout(self.graph)

        # Draw nodes with shell layout
        nx.draw_networkx_nodes(self.graph, shell_layout, node_color='skyblue', node_size=700)

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
g.add_edge(3, 8)
g.add_edge(3, 9)
g.add_edge(3, 10)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(4, 7)


# Perform DFS starting from vertex 2
print("DFS starting from vertex 2:")
g.dfs(2)
print()

# Perform BFS starting from vertex 2
print("BFS starting from vertex 2:")
g.bfs(2)
print()

# Visualize the graph
g.visualize()