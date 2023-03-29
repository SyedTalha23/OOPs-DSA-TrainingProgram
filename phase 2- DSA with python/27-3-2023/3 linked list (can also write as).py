class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      selected_node = self.headval
      while selected_node is not None:
         print (selected_node.dataval)
         selected_node = selected_node.nextval

list = SLinkedList()
e1=Node("Mon")
list.headval = e1
e2 = Node("Tue")
e3 = Node("Wed")

e1.nextval = e2
e2.nextval = e3

list.listprint()