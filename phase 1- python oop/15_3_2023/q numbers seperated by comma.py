'''
problem--> input:a string of comma seperated numbers,the numbers 5 and 8 are present in
the list. assume that 8 always comes after 8.
case1:add all numbers that do not lie between 5 and 8...
'''
num="3,2,6,5,1,4,8,9"
l=list(map(int,num.split(",")))
iof5=l.index(5)
iof8=l.index(8)
num1=sum(l[0:iof5])+sum(l[iof8+1:])
temp=list(map(str,l[iof5:iof8+1]))
num2="".join(temp)
op=int(num2)+num1
print(op)

#shortened version below

l=list(map(int,input().split(",")))
print(sum(l[0:l.index(5)])+sum(l[l.index(8)+1:])+"".join(list(map(str,l[l.index(5):l.index(8)+1]))))



