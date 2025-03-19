'''a(200) b(300) c(400) and d(500) pass this as in put node in fun and print its reverse as d c b a'''

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def print_reverse(nodes):
    stack = []
    
    while nodes:
        node = nodes.pop()
        stack.append(node)
    
    while stack:
        node = stack.pop()
        print(f"{node.name}({node.value})", end=" ")

a = Node('a', 200)
b = Node('b', 300)
c = Node('c', 400)
d = Node('d', 500)

nodes = [a, b, c, d]

print_reverse(nodes)
