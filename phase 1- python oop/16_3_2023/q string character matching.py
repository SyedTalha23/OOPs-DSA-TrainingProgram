s1=input()
s1=s1.replace(" ","")
s2=input()
s2=s2.replace(" ","")
l=[]
for i in s1:
    for j in s2:
        if i==j:
            l.append(i)
            break
l=set(l)
for i in list(l):
    print(i,end="")
if list(l)==[]:
    print(-1)
#I like Python
#Java is  a very popular language






'''
#shorter method below

s1=input()
s1=s1.replace(" ","")
s2=input()
s2=s2.replace(" ","")
for i in s1:
    if i in s2:
        print(i,end="")
'''