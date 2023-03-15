'''
problem statement: for each number in list_b, get the number and its position(index)
in mylist as are turn list of touples
'''

mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[[0,0]for i in range(len(list_b))]
x=0
for i in list_b:
    result[x]=[i,mylist.index(i)]
    x+=1
result=list(map(tuple,result))
print(result)
d={}
for i in result:
    d.update({i[0]:i[1]})
print(d)
