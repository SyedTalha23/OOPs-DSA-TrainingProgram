"""
Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India.40 min
They want to keep track of customers who buy fruits from them and also the billing process.


Write a python program to implement the class diagram given below.

RULES TO FOLLOW
=================
Class Description:
Fruit Info class:
fruit_name_list: Static list which contains the list of fruits available
fruit_price_list: Static list which contains the price/kg of fruits
The above two lists have one-to-one correspondence, initialize it with the data given in the table
get_fruit_price(fruit_name): Accept a fruit name and return its price/kg. If fruit is not available, return -1

Fruit Name	Apple	Guava	Orange	Grape	Sweet Lime
Price per Kg	200	80	70	110	60Purchase class:
Initialize static variable counter to 101
calculate_price(): Calculate and return total fruit price based on rules given below
For valid fruit name (hint: invoke get_fruit_price(fruit_name)),
Calculate price based on price/kg and quantity of the fruit purchased by the customer
If price/kg of the fruit is maximum among the fruits in fruit lists and quantity purchased is more than 1kg, apply 2% discount on calculated price
If price/kg of the fruit is minimum among the fruits in fruit lists and quantity purchased is 5kg or more, apply 5% discount on calculated price
If the customer is a "wholesale" customer, provide an additional 10% discount. Apply this discount on already discounted price, 
if any one of the above two points are applicable. Else apply it on calculated price
Auto-generate purchase id starting from 101 prefixed by “P”. Example – P101,P102 P103 etc.
Return final fruit price
Else, return -1.
Note:
Perform case sensitive string comparison 
There will be only one fruit with maximum price and one with minimum price

For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details"""

class FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            return FruitInfo.fruit_price_list[FruitInfo.fruit_name_list.index(fruit_name)]
        else:
            return -1

class Purchase:
    counter = 101
    
    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = "P" + str(Purchase.counter)
        Purchase.counter += 1
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
    
    def calculate_price(self):
        price_per_kg = FruitInfo.get_fruit_price(self.__fruit_name)
        if price_per_kg == -1:
            return -1
        else:
            total_price = price_per_kg * self.__quantity
            if price_per_kg == max(FruitInfo.fruit_price_list) and self.__quantity > 1:
                total_price *= 0.98
            elif price_per_kg == min(FruitInfo.fruit_price_list) and self.__quantity >= 5:
                total_price *= 0.95
            if self.__customer.get_cust_type() == 'wholesale':
                total_price *= 0.90
            return total_price
    
class Customer:
    def __init__(self, name, cust_type):
        self.__name = name
        self.__cust_type = cust_type
    
    def get_name(self):
        return self.__name
    
    def get_cust_type(self):
        return self.__cust_type

c = Customer("John", "wholesale")
p = Purchase(c, "Apple", 2)
print("Purchase ID:", p._Purchase__purchase_id)
print("Customer name:", c.get_name())
print("Customer type:", c.get_cust_type())
print("Fruit name:", p._Purchase__fruit_name)
print("Quantity:", p._Purchase__quantity)
print("Total price:", p.calculate_price())
