class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def front(self):
        if self.is_empty():
            return None
        return self.front_node.data

    def is_empty(self):
        return self.front_node is None

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        temp= self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None: 
            self.rear_node = None
        return temp


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)


print("Front element:", q.front())  
print("Check queue is empty:", q.is_empty())

print("Dequeue:", q.dequeue()) 
print("Front element:", q.front())  
print("Dequeue:", q.dequeue()) 
print("Dequeue:", q.dequeue()) 
print("Dequeue:", q.dequeue()) 

print("Front element:", q.front())  
