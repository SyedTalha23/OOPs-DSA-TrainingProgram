class Queue:
    def __init__(self, max_size):
        self.__max_size=max_size
        self.__elements=[]
        
    def is_full(self):
        if(len(self.__elements)==self.__max_size):
            return True
        return False
    
    def is_empty(self):
        if(len(self.__elements)==0):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__elements.append(data)
            
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements.pop(0)
            return data
        
    def display(self):
        for i in self.__elements:
            print(i)
    def get_max_size(self):
        return self.__max_size
    

queue1=Queue(4)
print("it is full",queue1.is_full())
print("it is empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("element deleted",queue1.dequeue())
queue1.display()

print("----------------------------------------------")

queue2=Queue(3)
queue2.enqueue(11)
queue2.enqueue(22)
queue2.enqueue(33)
queue2.dequeue()
queue2.dequeue()
queue2.display()
queue2.enqueue(44)
queue2.display()