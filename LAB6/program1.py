'''a(200) b(300) c(400) and d(500) pass this as in put node in fun and print its reverse as d c b a'''

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.next = None  # Points to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the linked list
    def append(self, name, value):
        new_node = Node(name, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(f"{current.name}({current.value})", end=" ")
            current = current.next
        print()

# Create the linked list
linked_list = LinkedList()

# Append nodes to the linked list
linked_list.append('a', 200)
linked_list.append('b', 300)
linked_list.append('c', 400)
linked_list.append('d', 500)

# Print the original list
print("Original list:")
linked_list.print_list()

# Reverse the linked list
linked_list.reverse()

# Print the reversed list
print("Reversed list:")
linked_list.print_list()

