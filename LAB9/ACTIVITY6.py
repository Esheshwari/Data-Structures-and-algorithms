class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 
class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None  
    
    def enqueue(self, data):
        new_node = Node(data)  
        if self.rear is None:
            self.front = self.rear = new_node  
            return
        self.rear.next = new_node  
        self.rear = new_node  
    def Front(self):
        if self.front is None:
            return None 
        return self.front.data  
    
    def is_empty(self):
        return self.front is None  
    
    def dequeue(self):
        if self.front is None:
            return None  
        temp = self.front  
        self.front = self.front.next  
        if self.front is None:
            self.rear = None 
        return temp.data 
    
def serve_customers():
    queue = Queue()
    
    
    customer_ids = [101, 102, 103, 104, 105]
    for customer_id in customer_ids:
        queue.enqueue(customer_id)
    
  
    while not queue.is_empty():
        customer_served = queue.dequeue()
        print(f"Serving customer with ID: {customer_served}")
    

    if queue.is_empty():
        print("The queue is now empty.")

serve_customers()
