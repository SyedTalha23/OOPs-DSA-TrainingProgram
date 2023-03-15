'''
def function1():
    print("its a function1")
function1()

def func2(a,b):
    c=a+str(b)
    return c
print(func2('1',2.2))
    
def func3(a):
    if a:
        print("true")
        print(type(a))
    else:
        print("false")
func3(True)
'''
'''
def func(arg1,arg2,arg3=777,arg4=999):
    print(f"arg1={arg1}")
    print(f"arg2={arg2}")
    print(f"arg3={arg3}")
    print(f"arg4={arg4}")
func(arg2=111,arg3=222,arg1=333)
'''
'''
#giving error because non default argument follows default argument,
#default aruments should be written on right side
def func(arg1=1111,arg2,arg3,arg4):
    print(f"arg1={arg1}")
    print(f"arg2={arg2}")
    print(f"arg3={arg3}")
    print(f"arg4={arg4}")
func(arg2=111,arg3=222,arg1=333,arg4=888)
'''



#variable number of arguments

def add(*var):
    total=0
    for i in var:
        total=total+i
    print(total)
add(1,2)
add(11,22,33,44)
add(100,300,500,700,900)

        
    
