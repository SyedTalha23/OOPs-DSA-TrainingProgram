num=int(input())
x=True
while(x):
    temp=str(num+1)
    if temp==temp[::-1]:
        x=False
    num+=1
print(temp)


