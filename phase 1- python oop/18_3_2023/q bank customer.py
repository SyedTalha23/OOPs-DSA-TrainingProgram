'''A bank has many customers and each customer has a bank account
There are also privileged customers 
who can earn bonus points for each of their transaction. 
This scenario is depicted through the below class diagram.
30 min

Customer
- customer_id
- customer_name
- age
- account
_init_(customer_id, customer_name, age, account)
+ withdraw(amount)
+ take_card()
+ get_customer_id()
+ get_customer_name()
+ get_age()
+ get_account()
Account
- account_type
- balance
- min_balance
_init_(account_type,balance,min_balance)
+ get_account_type()
+ get_balance()
+ get_min_balance()
+ set_balance(balance)
PrivilegedCustomer
- bonus_points
_init_ (customer_id, customer_name, age, account, 
bonus_points)
+ withdraw(amount)
+ get_bonus_points()
- increase_bonus()
OverdrawException
LimitReachedException

RULES TO FOLLOW
================
Customer:
withdraw(amount): This method should reduce the account balance based on the amount withdrawn. 
Raise the following exceptions based on the given conditions.
OverdrawException - If the amount to be withdrawn is greater than account balance.
LimitReachedException - If the balance amount is less than minimum account balance.
take_card(): Displays the message "Take card out from the ATM".
PrivilegedCustomer:
increase_bonus(): If the account balance is greater than 1000, increase the bonus points by 10, else increase it by 2.
withdraw(amount): Invoke the parent class withdraw() method and increase the bonus points by calling increase_bonus() method, if no exceptions occured.
If exceptions occur, display relevant messages. Ensure that the card is taken out from the ATM under any situation.

Write a Python program to create a new PrivilegedCustomer with below details:
Customer Id: 100
Customer Name: Gopal
Age: 43
Bonus Points: 100
Account Type: Savings
Account Balance: 1000
Account minimum: 500

The customer should be able to withdraw money and also display the bonus points of the customer after the withdraw.'''





class customer:
    def __init__(self,cid,cname,cage,account):
        self.customer_id=cid
        self.customer_name=cname
        self.age=cage
        self.account=account
    def withdraw(self,amount):
        self.amount=amount
        self.temp=self.account.balance-self.amount
        if self.temp<0:
            print("OverdrawException")
        elif self.temp<self.account.min_balance:
            print("LimitReachedException")
        else:
            self.account.balance=self.account.balance-self.amount
            print(f"remaining balance : {self.account.balance}")
            self.take_card()
    def take_card(self):
        print("take card out of the atm")
    def get_customer_id(self):
        return self.customer_id
    def get_age(self):
        return self.age
    def get_account(self):
        return self.account
class account:
    def __init__(self,account_type,balance,min_balance):
        self.account_type=account_type
        self.balance=balance
        self.min_balance=min_balance
    def get_account_type(self):
        return self.account_type
    def get_balance(self):
        return self.balance
    def get_min_balance(self):
        return self.min_balance
    def set_balance(self,balance):  
        self.balance=balance
class privilegedcustomer(customer):
    def __init__(self,cid,cname,cage,account,bonus):
        self.customer_id=cid
        self.customer_name=cage
        self.age=cage
        self.account=account
        self.bonus_points=bonus
    def withdraw(self,amount):
        self.amount=amount
        self.temp=self.account.balance-self.amount
        if self.temp<0:
            print("OverdrawException")
        elif self.temp<self.account.min_balance:
            print("LimitReachedException")
        else:
            self.account.balance=self.account.balance-self.amount
            print(f"remaining balance : {self.account.balance}")
            super().take_card()
            self.increase_bonus()
    def get_bonus_points(self):
        return self.bonus_points
    def increase_bonus(self):
        if self.account.balance>1000:
            self.bonus_points=self.bonus_points+10
        else:
            self.bonus_points=self.bonus_points+2
        
    

a1=account("savings",1000,500)
c1=privilegedcustomer(100,"gopal",43,a1,100)
c1.withdraw(200)
print(f"bonus points ={c1.get_bonus_points()}")

print("----------------------------------------")

a2=account("savings",5000,1000)
c2=customer(101,"bbb",21,a2)
c2.withdraw(3000)

print("-----------------------------------------")

a3=account("savings",1000,500)
c3=privilegedcustomer(100,"cccc",43,a3,110)
c3.withdraw(2000)
print(f"bonus points ={c3.get_bonus_points()}")





            


    
