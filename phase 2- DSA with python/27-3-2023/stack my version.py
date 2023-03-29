class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[]

    def is_full(self):
        if ( len(self.__elements)==self.__max_size):
            return True
        return False
    def is_empty(self):
        if(len(self.__elements)==0):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__elements.append(data)
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            data=self.__elements.pop()
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            for i in self.__elements[::-1]:
                print(i)
    def get_max_size(self):
        return self.__max_size
    
    
stack1=Stack(4)
stack1.push(11)
stack1.push(22)
stack1.push(33)
stack1.push(44)
stack1.push(44)
stack1.display()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.display()