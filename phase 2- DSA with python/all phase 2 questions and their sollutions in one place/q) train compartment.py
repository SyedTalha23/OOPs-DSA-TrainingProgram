"""11.A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where 
data in each node refers to a compartmentList1.
A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating 
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:

count_compartments()- returns the total number of compartments in the train
check_vacancy()-returns the count of the compartments in which more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where data in each node refers to a compartmentList1.

compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)

"""
class node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class sLinkedList:
    def __init__(self):
        self.headNode=None
    
    def insertAtEnd(self,data):
        if self.headNode==None:
            self.headNode=node(data)
            return
        itr=self.headNode
        while itr.nextNode is not None:
            itr=itr.nextNode
        itr.nextNode=node(data)
    
    def traverseList(self):
        itr=self.headNode
        while itr is not None:
            print(itr.data)
            itr=itr.nextNode
    
    def length(self):
        count=0
        itr=self.headNode
        while itr is not None:
            itr=itr.nextNode
            count+=1
        print(count)
    


class train:
    def __init__(self,name,compartmentList):
        self.__name=name
        self.__compartmentList=compartmentList
    
    def get_train_name(self):
        return self.__name
    
    def get_compartment_list(self):
        print("compartments= ")
        self.__compartmentList.traverseList()
    
    def count_compartments(self):
        print("number of compartments= ",end="")
        self.__compartmentList.length()

    def check_vacancy(self):
        itr=self.__compartmentList.headNode
        counter=0
        while itr is not None:
            temp=itr.data
            if temp[1]/temp[2]<0.50:
                counter+=1
            itr=itr.nextNode
        print("compartments with more than 50% vacancy= ",counter)


    
compartmentList1=sLinkedList()
compartmentList1.insertAtEnd(["SL",250,400])
compartmentList1.insertAtEnd(["2AC",125,280])
compartmentList1.insertAtEnd(["3AC",120,300])
compartmentList1.insertAtEnd(["FC",160,300])
compartmentList1.insertAtEnd(["1AC",100,210])


train1=train("aaa",compartmentList1)
print("train name= ",train1.get_train_name())
train1.get_compartment_list()
train1.count_compartments()
train1.check_vacancy()