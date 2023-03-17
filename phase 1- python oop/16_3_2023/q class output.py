class example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
    
class customer: 
    def __init__(self):
       self.cust_id=100 
c1=customer()
print(c1.cust_id)


