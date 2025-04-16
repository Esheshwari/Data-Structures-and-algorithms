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

    def display(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")

graph = Graph()

edges = [(0, 1), (0, 2), (2, 3), (3, 4), (4, 1)]

for v, w in edges:
    graph.add_edge(v, w)

graph.display()
