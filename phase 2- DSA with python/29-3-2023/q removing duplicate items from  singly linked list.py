class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        selected_node = self.headval
        while selected_node != None:
            print (selected_node.dataval)
            selected_node = selected_node.nextval
    
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.headval is None:
            self.headval=new_node
            return
        currentNode=self.headval
        while currentNode.nextval is not None:
            currentNode=currentNode.nextval
        currentNode.nextval=new_node
    
    def removeDuplicates(self):
        currentNode=self.headval
        while currentNode.nextval is not None:
            while currentNode.dataval==currentNode.nextval.dataval:
                currentNode.nextval=currentNode.nextval.nextval
            currentNode=currentNode.nextval
        



q1=SLinkedList()
list(map(q1.insertAtEnd,input().split()))
q1.listprint()
print("==========")
q1.removeDuplicates()
q1.listprint()
      