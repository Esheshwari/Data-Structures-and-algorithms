class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, v, w):
        if v not in self.adj_list:
            self.adj_list[v] = []
        if w not in self.adj_list:
            self.adj_list[w] = []
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

# Example usage:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)

# Print the adjacency list representation
graph.print_graph()
