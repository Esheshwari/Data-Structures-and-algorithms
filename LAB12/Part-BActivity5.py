from collections import deque

# Graph class that uses adjacency list
class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to hold adjacency list
    
    # Method to add an edge to the graph (directed or undirected)
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        # For undirected graph, we add both u -> v and v -> u
        self.graph[u].append(v)
        self.graph[v].append(u)  # comment this line for directed graph

    # Method to perform BFS starting from a specific vertex
    def bfs(self, start_vertex):
        # Set of visited nodes
        visited = set()
        
        # Queue for BFS
        queue = deque([start_vertex])
        
        # Mark the start vertex as visited
        visited.add(start_vertex)
        
        # List to store the order of traversal
        traversal_order = []
        
        # Process the queue until it is empty
        while queue:
            vertex = queue.popleft()  # Dequeue the next vertex
            traversal_order.append(vertex)  # Add it to the traversal order
            
            # Visit all adjacent vertices of the current vertex
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)  # Enqueue unvisited neighbors
        
        # Print the order of traversal
        print("BFS Traversal Order:", traversal_order)

# Example of using the Graph class and performing BFS
g = Graph()

# Add edges to the graph (undirected graph)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(4, 7)

# Perform BFS starting from vertex 0
g.bfs(0)
