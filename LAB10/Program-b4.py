'''Create a class/structure Graph to represent a graph using an adjacency list. Implement the following  operations: 
1. add_edge(v, w): Add an edge between vertices v and w. 
Solution: '''
class Graph: 
 def __init__(self): 
 self.adj_list = {} 
 def add_edge(self, u, v): 
 if u not in self.adj_list: 
 self.adj_list[u] = [] 
 if v not in self.adj_list: 
 self.adj_list[v] = [] 
 self.adj_list[u].append(v) 
 self.adj_list[v].append(u) 
# Example usage: 
graph = Graph() 
graph.add_edge(1, 2) 
graph.add_edge(1, 3) 
graph.add_edge(2, 4) 
graph.add_edge(3, 4) 
graph.add_edge(4, 5) 



