#input:rhdt:246,ghftd:1246

s=input()
l1=list(s.split(","))
l2=[]
digitsq=0
for i in l1:
    temp=list(i.split(":"))
    for j in temp:
        l2.append(j)
for i in range(len(l2)):
    if i%2!=0:
        temps=str(l2[i])
        for j in temps:
            digitsq=digitsq+int(j)*int(j)
        if digitsq%2==0:
            l2[i-1]=str(l2[i-1])[-1]+str(l2[i-1])[:-1]
        else:
            l2[i-1]=str(l2[i-1])[2:]+str(l2[i-1])[:2]
        digitsq=0
for i in range(len(l2)):
    if i%2==0:
        print(l2[i])


#trainers solution below
s=input().split(",") #rhdt:246, ghftd: 1246
stt=[]
numm= []
for i in s:
    s1,n=i.split(":")
    stt.append(s1) #stt= [rhdt, ghftd]
    numm.append(n) #numm= [246, 1246]
def rotate(ss,n) : #ss=rhdt, n=246
    n=str(n)
    s=0
    for i in n:#
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1] # rhdt
    else:
        return ss[2:]+ss[:2]

for i in range (len (numm) ) : #i=0
    print (rotate (stt[i],numm[i]))
