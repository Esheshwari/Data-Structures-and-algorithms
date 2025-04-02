'''Activity 6: 
Write a program to create a class Node to represent a node in a singly linked list. Each node  should have two attributes: data and next. Then, create a class Queue to represent the queue  itself. Implement the following operations: 
1. enqueue(data): Add a new node with the given data to the end of the queue. 
2. Front(): Return the data of the front node without removing it. If the queue is empty, return  None. 
3. is_empty(): Return True if the queue is empty, otherwise return False. 
4. dequeue(): Remove and return the front node from the queue. If the queue is empty, return  None. 
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def Front(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return self.front is None

    def dequeue(self):
        if self.front is None:
            print("empty")
        else: 
            temp=self.front
            self.front=temp.next
            deleted_item=temp.data
            del(temp)
            temp=None
            print(f'dequeued item is {deleted_item}')
# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.Front())  
print(q.dequeue()) 
print(q.is_empty())  
print(q.dequeue())  
print(q.dequeue())  
print(q.is_empty())  
