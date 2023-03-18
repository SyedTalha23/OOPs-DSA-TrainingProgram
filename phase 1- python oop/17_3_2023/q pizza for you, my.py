#need to use inheritance in this code,
'''
class customer:
    def __init__(self,q):
        self.quantity=q
    def validate_quantity(self):
        if self.quantity>=1 and self.quantity<=5:
            return True
        else:
            return False
class pizzaservice(customer):
    counter=100
    def __init__(self,ptype,topping):
        additional_topping=topping
        self.cost=None
        self.service_id=None
    def validate_pizza_type(self):
        if self.ptype=="small" or self.ptype=="medium":
            return True
        else:
            False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type():
            if self.ptype=="small" and self.additional_topping==True:
                self.cost=185
            elif self.ptype=="small" and self.additional_topping==False:
                self.cost=150
            elif self.ptype=="medium" and self.additional_topping==True:
                self.cost=250
            else:
                self.cost=200
            self.service_id=self.ptype[0]+str(pizzaservice.counter)
            pizzaservice.counter+=1
        else:
            self.cost=-1

class doordelivery(pizzaservice):
    def validate_distance_in_kms(self):
        if self.distance>=1 and self.validate_distance_in_kms<=10:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            return super().calculate_pizza_cost()
'''