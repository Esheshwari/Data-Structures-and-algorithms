#after adding in program1 traverse this
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, create a single node that points to itself
            self.head = new_node
            new_node.next = self.head
        else:
            # Traverse the list to find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            # Insert the new node at the beginning
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
    def traverse (self):
        if self.head is None: 
            print("Circular linked list is empty.") 
            return 
        current = self.head
        while True: 
           print(current.data, end=" -> ")         
           current  = current.next
           if current == self.head: 
                break 
        print("(Back to Head)") 

# Create a circular linked list
cll = CircularLinkedList()

# Insert data into the list
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_beginning(30)
cll.traverse()
