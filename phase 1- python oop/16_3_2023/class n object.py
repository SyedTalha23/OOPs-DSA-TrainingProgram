'''
class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    #def __str__(self):
        # "shoe with price: " + str(self.price) + "and material: " +self.material
    
s1=shoe(1000,"canvas")
print(s1)
print(s1.price,s1.material)
print("the unique if of the object",id(s1))

class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
         return "shoe with price: " + str(self.price) + "and material: " +self.material
    
print("======================================================")
    
s1=shoe(1000,"canvas")
print(s1)
print(s1.price,s1.material)
print("the unique if of the object",id(s1))

print("===========================================================")
class mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        self.display()
        print("calculating price")

mobile().purchase()
m1=mobile()
m2=mobile()
print(m1)
print(m2)
m1=m2
print(m1)
print(m2)

class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price= self.price - self.price * (discount/100)
        print("Total price of",self.brand, "mobile is", self.total_price)
    def amount_returned(self):
        return self.total_price
        
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())

'''
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance+=amount
    def show_balance(self):
        print("The balance is ",self.wallet_balance)
        
c1=Customer(100, "Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()