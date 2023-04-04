"""
Write a python program to reverse a linked list containing 
integer data.
Use the LinkedList class and methods in it to implement the
 above program."""

class node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class linkedList:
    def __init__(self):
        self.headNode=None
    
    def insert(self,data):
        if self.headNode==None:
            self.headNode=node(data)
            return
        itr=self.headNode
        while itr.nextNode!=None:
            itr=itr.nextNode
        itr.nextNode=node(data)    
    
    def printList(self):
        if self.headNode==None:
            print("linkedlist is empty")
        itr=self.headNode
        while itr!=None:
            print(itr.data,end=" ")
            itr=itr.nextNode
        print()
    
    def reverseList(self):
        if self.headNode==None:
            return
        prev = None
        itr = self.headNode
        while(itr is not None):
            next = itr.nextNode
            itr.nextNode = prev
            prev = itr
            itr = next
        self.headNode = prev


    

ll1=linkedList()
ll1.insert(1)
ll1.insert(2)
ll1.insert(3)
ll1.insert(4)
ll1.insert(5)
ll1.printList()
ll1.reverseList()
ll1.printList()

