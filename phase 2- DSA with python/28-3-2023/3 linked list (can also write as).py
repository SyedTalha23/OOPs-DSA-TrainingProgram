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

   def AtBegining(self,newdata):
      NewHeadNode = Node(newdata)
      NewHeadNode.nextval = self.headval
      self.headval = NewHeadNode
   
   def AtEnd(self, newdata):
      NewEndNode = Node(newdata)
      if self.headval == None:
         self.headval = NewEndNode
         return
      CurrentNode = self.headval
      while CurrentNode.nextval != None:
         CurrentNode = CurrentNode.nextval
      CurrentNode.nextval=NewEndNode
   
   def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return
      NewNode = Node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode
   
   
   


list = SLinkedList()
n1=Node("Mon")
list.headval = n1
n2 = Node("Tue")
n3 = Node("Wed")

n1.nextval = n2
n2.nextval = n3

list.AtBegining("Sun")

list.AtEnd("thu")

list.Inbetween(list.headval.nextval,"Fri")   

list.listprint()
