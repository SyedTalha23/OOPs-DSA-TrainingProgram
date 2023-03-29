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
    
q1=Queue(3)
map(q1.enqueue(),input().split(","))
q1.display()
