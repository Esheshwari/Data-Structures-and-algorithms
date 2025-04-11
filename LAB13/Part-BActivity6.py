class Graph:
    def __init__(self, vertices):
        # Initialize the graph with a number of vertices and an empty adjacency list
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}  # Adjacency list representation of the graph

    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v (directed)"""
        self.graph[u].append(v)

    def _dfs(self, v, visited, rec_stack):
        """
        Helper DFS function to detect a cycle.
        - visited: list to track visited nodes.
        - rec_stack: recursion stack to track nodes in the current DFS path.
        """
        # Mark the current node as visited and add it to the recursion stack
        visited[v] = True
        rec_stack[v] = True

        # Recur for all adjacent vertices
        for neighbor in self.graph[v]:
            if not visited[neighbor]:  # If not visited, recurse deeper
                if self._dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:  # If neighbor is in the recursion stack, cycle is detected
                return True

        # Remove from recursion stack
        rec_stack[v] = False
        return False

    def detect_cycle(self):
        """
        Method to check if the graph contains a cycle.
        Returns True if a cycle is detected, else False.
        """
        # Initialize visited and recursion stack arrays
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        # Run DFS from all unvisited nodes
        for node in range(self.vertices):
            if not visited[node]:
                if self._dfs(node, visited, rec_stack):
                    return True
        return False

# Example Usage
g = Graph(4)

# Add directed edges to the graph
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)  # This creates a cycle (1 -> 2 -> 3 -> 1)

# Check if there is a cycle
if g.detect_cycle():
    print("Cycle detected in the graph.")
else:
    print("No cycle detected in the graph.")
