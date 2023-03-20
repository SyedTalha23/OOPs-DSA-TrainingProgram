'''question: A bank has many customers and each customer has a bank acc
There are also privileged customers 
who can earn bonus points for each of their transaction. 
This scenario is depicted through the below class diagram.
30 min

Customer
- customer_id
- customer_name
- age
- acc
_init_(customer_id, customer_name, age, acc)
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
_init_ (customer_id, customer_name, age, acc, 
bonus_points)
+ withdraw(amount)
+ get_bonus_points()
- increase_bonus()
OverdrawException
LimitReachedException

RULES TO FOLLOW
================
Customer:
withdraw(amount): This method should reduce the acc balance based on the amount withdrawn. 
Raise the following exceptions based on the given conditions.
OverdrawException - If the amount to be withdrawn is greater than acc balance.
LimitReachedException - If the balance amount is less than minimum acc balance.
take_card(): Displays the message "Take card out from the ATM".
PrivilegedCustomer:
increase_bonus(): If the acc balance is greater than 1000, increase the bonus points by 10, else increase it by 2.
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



class Account:
    def __init__(self, account_type, balance, min_balance):
        self.account_type = account_type
        self.balance = balance
        self.min_balance = min_balance
        
    def get_account_type(self):
        return self.account_type
    
    def get_balance(self):
        return self.balance
    
    def get_min_balance(self):
        return self.min_balance
    
    def set_balance(self, balance):  
        self.balance = balance


class Customer:
    def __init__(self, customer_id, customer_name, age, Account):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.age = age
        self.Account = Account
        
    def withdraw(self, amount):
        temp = self.Account.balance - amount
        try:
            if temp < 0:
                raise OverdrawException("The amount to be withdrawn is greater than the Account balance")
            elif temp < self.Account.min_balance:
                raise LimitReachedException("The balance amount is less than minimum Account balance")
            else:
                self.Account.balance -= amount
                print(f"Remaining balance: {self.Account.balance}")
                return True
        except (OverdrawException, LimitReachedException) as e:
            print(e)
            return False
        finally:
            self.take_card()
            

    def take_card(self):
        print("Take card out from the ATM")
    
    def get_customer_id(self):
        return self.customer_id
    
    def get_customer_name(self):
        return self.customer_name
    
    def get_age(self):
        return self.age
    
    def get_account(self):
        return self.Account
    

class PrivilegedCustomer(Customer):
    def __init__(self, customer_id, customer_name, age, Account, bonus_points=0):
        super().__init__(customer_id, customer_name, age, Account)
        self.bonus_points = bonus_points
        
    def withdraw(self, amount):
            if super().withdraw(amount):
                self.increase_bonus()
            
    
    def get_bonus_points(self):
        return self.bonus_points
    
    def increase_bonus(self):
        if self.Account.balance > 1000:
            self.bonus_points += 10
        else:
            self.bonus_points += 2
            

class OverdrawException(Exception):
    pass


class LimitReachedException(Exception):
    pass
a1=Account("savings",1000,500)
c1=PrivilegedCustomer(100,"gopal",43,a1,100)
c1.withdraw(200)
print(f"bonus points ={c1.get_bonus_points()}")

print("----------------------------------------")

a2=Account("savings",5000,1000)
c2=Customer(101,"bbb",21,a2)
c2.withdraw(3000)

print("-----------------------------------------")

a3=Account("savings",1000,500)
c3=PrivilegedCustomer(102,"cccc",43,a3,110)
c3.withdraw(2000)
print(f"bonus points ={c3.get_bonus_points()}")

print("---------------------------------------")

a4=Account("savings",5000,1000)
c4=Customer(103,"ddd",29,a4)
c4.withdraw(6000)

