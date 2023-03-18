class Student:
    def _init_(self):
        self.__s_id=None
        self.__s_age=None
        self.__s_marks=None
    def validate_marks(self):
        if(self.__s_marks>0 and self.__s_marks<100):
            return True
        else:
            return False
    def validate_age(self):
        if(self.__s_age>20):
            return True
        else:
            return False
    def check_qualification(self):
        if(self.validate_marks() and self.validate_age() and self.__s_marks>65):
            return True
        else:
            return False
        
        
    def choose(self,c_id):
        if self.check_qualification():
            if(c_id == 1001):
                f = 25575.0
                if(self.__s_marks>85):
                    fees_to_paid = f - f*0.25
                    print("fees to be paid is ",fees_to_paid)
                else:
                    print("fees to be paid is ",f)
            if(c_id == 1002):
                f = 15500.0
                if(self.__s_marks>85):
                    fees_to_paid = f - f*0.25
                    print("fees to be paid is ",fees_to_paid)
                else:
                    print("fees to be paid is ",f)
                    
        else:
            print("not eligible")
    def set_id(self,x):
        self.__s_id = x
    def get_id(self):
        return self.__s_id
    def set_age(self,x):
        self.__s_age = x
    def get_age(self):
        return self.__s_age
    def set_marks(self,x):
        self.__s_marks = x
    def get_marks(self):
        return self.__s_marks

    
s1=Student()
s1.set_id(1010)
s1.set_age(13)
s1.set_marks(66)
s1.choose(1001)

s2=Student()
s2.set_id(1011)
s2.set_age(36)
s2.set_marks(99)
s2.choose(1001)


