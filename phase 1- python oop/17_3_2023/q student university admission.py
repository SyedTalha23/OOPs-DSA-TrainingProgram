class student:
    def __init__(self):
        print("obj created")
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.course=None
        self.fees=None
        self.eligibility_status=None
    def set_details(self,sid,sm,sa):
        self.__student_id=sid
        self.__marks=sm
        self.__age=sa
    def validate_marks(self):
        if 100>=self.__marks>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks>=65:
                return True
        else:
            return False
    def choose_course(self):
        if self.check_qualification():
            self.fees=None
            self.eligibility_status="elligible"
            self.course=int(input("\nyou are eligible for admission,\ninput 1001 to choose course 1001 (default fees 25575.0)\ninput 1002 to choose course 1002 (default fees 15500.0)\nyour choice: "))
            if self.course==1001 and self.__marks>85:
                self.fees =25575.0- 0.25*25575.0
            elif self.course==1001 and self.__marks<=85:
                self.fees =25575.0
            elif self.course==1002 and self.__marks>85:
                self.fees =15500.0- 0.25*15500.0
            elif self.course==1002 and self.__marks<=85:
                self.fees =15500.0
            print(f"\nyou have joined course {self.course} and your fees is {self.fees}")
        else:
            print("not elligible")
            self.eligibility_status="not elligible"
    def get_all_data(self):
        l=["id:",self.__student_id,"marks:",self.__marks,"age:",self.__age,"eligibility:",self.eligibility_status,"course:",self.course,"fees:",self.fees]
        return l

           
n=int(input("enter number of students: "))
studentlist=[]
for i in range(1,n+1):
    studentlist.append("s"+str(i))
print(studentlist)
for i in range(len(studentlist)):
    studentlist[i]=student()
for i in range(len(studentlist)):
    studentlist[i].set_details(int(input(f"enter id for student{i+1}: ")),int(input(f"enter marks for student{i+1}: ")),int(input(f"enter age for student{i+1}: ")))
    studentlist[i].choose_course()
    print()
for i in range(len(studentlist)):
    d=studentlist[i].get_all_data()
    print("details for student",i+1,"=",*d)


