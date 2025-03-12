'''Write a program to create a class/structure DoublyNode to represent a node in a doubly linked list.  Each node should have three attributes: data, next, and prev. Then, create a class/structure  DoublyLinkedList to represent the linked list itself. Implement the following operations: 
1. insert_at_beginning(data): Insert a new node with the given data at the beginning of the list. 2. insert_at_end(data): Insert a new node with the given data at the end of the list. 3. traverse_forward(): Traverse the list forward and print the data of each node. '''
class DoublyNode:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None  

    # Method to insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = DoublyNode(data) 
        if self.head is None: 
            self.head = new_node 
        else:
            new_node.next = self.head  
            self.head.prev = new_node  
            self.head = new_node 

    # Method to insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = DoublyNode(data) 
        
        if self.head is None: 
            self.head = new_node 
        else:
            current = self.head
            while current.next:
                current = current.next
          
            current.next = new_node
            new_node.prev = current  

   
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print()  



dll = DoublyLinkedList()

dll.insert_at_beginning(10)
print("After inserting 10 at the beginning:")
dll.traverse_forward()

dll.insert_at_beginning(20)
print("After inserting 20 at the beginning:")
dll.traverse_forward()

dll.insert_at_beginning(30)
print("After inserting 30 at the beginning:")
dll.traverse_forward()

# Insert 40 at the end
dll.insert_at_end(40)
print("After inserting 40 at the end:")
dll.traverse_forward()

# Insert 50 at the end
dll.insert_at_end(50)
print("After inserting 50 at the end:")
dll.traverse_forward()

# Final traverse forward to show the complete list
print("Final traversal of the list forward:")
dll.traverse_forward()
'''output
After inserting 10 at the beginning:
10 <-> 
After inserting 20 at the beginning:
20 <-> 10 <-> 
After inserting 30 at the beginning:
30 <-> 20 <-> 10 <-> 
After inserting 40 at the end:
30 <-> 20 <-> 10 <-> 40 <-> 
After inserting 50 at the end:
30 <-> 20 <-> 10 <-> 40 <-> 50 <-> 
Final traversal of the list forward:
30 <-> 20 <-> 10 <-> 40 <-> 50 <-> '''
