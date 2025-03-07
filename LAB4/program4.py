'''Write a program to create a class/structure Node to represent a node in a singly linked list. Each  node should have two attributes: data and next. Implement the following operations:  
1. insert_at_beginning(data): Insert a new node with the given data at the beginning of the list. 2. insert_at_end(data): Insert a new node with the given data at the end of the list. 
3. delete_node(data): Delete the first node in the list that contains the given data.  
4. traverse(): Traverse the list and print the data of each node 
Solution: '''
class Node: 
 def __init__(self, data): 
 self.data = data 
 self.next = None 
class LinkedList: 
 def __init__(self): 
 self.head = None 
  
 def insert_at_beginning(self, data): 
 new_node = Node(data) 
 new_node.next = self.head 
 self.head = new_node 
  
 def insert_at_end(self, data): 
 new_node = Node(data) 
 if not self.head: 
 self.head = new_node 
 return 
 last = self.head 
 while last.next: 
 last = last.next 
 last.next = new_node 
  
 def delete_node(self, data): 
 current = self.head 
  
 if current and current.data == data: 
 self.head = current.next 
 current = None 
 return 
  
 prev = None 
 while current and current.data != data: 
 prev = current 
 current = current.next 
  
 if current is None: 
 return 
  
 prev.next = current.next 
 current = None 
  
 def traverse(self): 
 current = self.head 
 while current: 
 print(current.data, end=" -> " if current.next else "")  current = current.next 
 print() 
# Example usage: 
linked_list = LinkedList() 
# Insert elements at the beginning 
linked_list.insert_at_beginning(10) 
linked_list.insert_at_beginning(20) 
print("Linked list after inserting 20, 10 at the beginning:") linked_list.traverse() 
# Insert elements at the end 
linked_list.insert_at_end(30) 
linked_list.insert_at_end(40) 
print("\nLinked list after inserting 30, 40 at the end:")

linked_list.traverse() 
# Delete a node 
linked_list.delete_node(20) 
print("\nLinked list after deleting node with data 20:") linked_list.traverse() 
# Traverse the list 
print("\nTraversing the linked list:") 
linked_list.traverse() 
