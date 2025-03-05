'''Activity 4: 
Write a program to create a class/structure Node to represent a node in a singly linked list. Implement the following operation: 
1. append_node(data): appends node at the end 
2. search_node(data): search for a node with a particular value 
3. display_list(): prints the list'''
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def search_node(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
llist = LinkedList()
llist.append_node(10)
llist.append_node(20)
llist.append_node(30)
llist.append_node(40)
llist.display_list()

print("Search 20:", llist.search_node(20))
print("Search 50:", llist.search_node(50))
#output
'''10 -> 20 -> 30 -> 40 -> None
Search 20: True
Search 50: False'''
