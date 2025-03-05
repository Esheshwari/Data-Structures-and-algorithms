'''Write a program to create a class/structure Node to represent a node in a singly linked list. Each  node should have two attributes: data and next. Implement the following operations
1. insert_at_beginning(data): Insert a new node with the given data at the beginning of the list. 2. insert_at_end(data): Insert a new node with the given data at the end of the list. 
3. delete_node(data): Delete the first node in the list that contains the given data.  
4. traverse(): Traverse the list and print the data of each node '''


class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_beginning(5)
llist.display()

llist.delete_node(20)
llist.display()

#output:
5 -> 10 -> 20 -> 30 -> None
5 -> 10 -> 30 -> None
