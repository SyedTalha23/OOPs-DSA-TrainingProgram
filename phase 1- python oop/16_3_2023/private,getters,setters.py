class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance #private instance variable
    def set_balance(self,amount): #setter
        if amount < 50000 and amount > 0:
            self.__wallet_balance+=amount
    def get_balance(self): #getter
        return self.__wallet_balance
        
c1=Customer(100, "Gopal",24,1000)
c1.set_balance(500)
print(c1.get_balance())

print("=====================================")

class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length

dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length",dam1.get_length())