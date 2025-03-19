'''a(200) b(300) c(400) and d(500) pass this as in put node in fun and print its reverse as d c b a'''

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Function to print nodes in reverse order without using .reverse()
def print_reverse(nodes):
    # Iterate over the list from the last node to the first node
    for i in range(len(nodes) - 1, -1, -1):
        node = nodes[i]
        print(f"{node.name}({node.value})", end=" ")

# Create node objects
a = Node('a', 200)
b = Node('b', 300)
c = Node('c', 400)
d = Node('d', 500)

# Put nodes into a list
nodes = [a, b, c, d]

# Call the function to print in reverse
print_reverse(nodes)
