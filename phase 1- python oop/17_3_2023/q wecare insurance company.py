class wecare:
    def __init__(self): 
        self.__vid=None
        self.__vtype=None
        self.__vcost=None
        self.__vpremium=None
    def set_details(self,vid,vtype,vcost):
        self.__vid=vid
        self.__vtype=vtype
        self.__vcost=vcost
    def premium_calc(self):
        if self.__vtype=="Two Wheeler":
            self.__vpremium=self.__vcost*0.02
        elif self.__vtype=="Four Wheeler":
            self.__vpremium=self.__vcost*0.06
        else:
            print("invalid")

    def get_premium_value(self):
        self.premium_calc()
        return self.__vpremium
    def get_vid(self):
        return self.__vid

v1=wecare()
v1.set_details(1,"Two Wheeler",100)
print(f"the premium for vehicle id {v1.get_vid()}=",v1.get_premium_value())
v2=wecare()
v2.set_details(2,"Four Wheeler",100)
print(f"the premium for vehicle id {v2.get_vid()}=",v2.get_premium_value())

        


    
