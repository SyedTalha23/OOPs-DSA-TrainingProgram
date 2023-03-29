'''Given two queues, one integer queue and another character queue, write a python program to merge them to form a single
queue.Follow the below rules for merging:
Merge elements at the same position starting with the integer queue. 
If one of the queues has more elements than the other, add all the additional elements at the end of the output queue.
Note: max_size of the merged queue should be the sum of the size of both the queues.

For example
Input-- queue1:3,6,8  queue2: b,y,u,t,r,o
Output -- 3,b,6,y,8,u,t,r,o
'''

class Queue:
    def __init__(self, max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
            
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
        
    def display(self):
        for index in range(self.__front,self.__rear):
            print(self.__elements[index],end=",")
        print(self.__elements[-1])
    def get_max_size(self):
        return self.__max_size
    

l1=list(input().split(","))
l2=list(input().split(","))
q1=Queue(len(l1))
q2=Queue(len(l2))

for i in l1:
    q1.enqueue(i)
for j in l2:
    q2.enqueue(j)


q3=Queue(len(l1)+len(l2))
ctr=0
for i in range(len(l1)+len(l2)):
    if i%2==0 and ctr<q1.get_max_size():
        q3.enqueue(q1.dequeue())
        ctr+=1
    else:
        q3.enqueue(q2.dequeue())
q3.display()
