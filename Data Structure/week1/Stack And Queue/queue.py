class Queue:
    def __init__(self):
        self.queue=[]
    #Add an element
    def Enqueue(self,value):
        self.queue.append(value)
    #Remove an element
    def Dequeue(self,value):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    #Display queue
    def Display(self):
        print(self.queue)
    
    def Size_Queue(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()