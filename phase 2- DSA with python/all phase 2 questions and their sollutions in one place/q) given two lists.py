'''Given two lists,both having String elements, write a python program using python lists to create a new string as per the
rule given below:
    
The first element in list1 should be merged with last element in list2, second element in list1 should be merged with
second last element in list2 and so on. If an element in list1/list2 is None, then the corresponding element in the other
list should be kept as it is in the merged list.

Sample Input
list1=['A','app','a','d','ke','th','doc','awa']
a,app,a,d,ke,th,doc,awa
list2=['y','tor','e','eps','ay',None,'le','n']
y,tor,e,eps,ay,None,le,n

Expected Output
"An apple a day keeps doctor away"

'''

l1=list(input().split(","))
l2=list(input().split(","))
l=len(l1)
for i in range(l):
    for j in range(l):
        if i+j==l-1:
            if l2[j]=="None":
                print(l1[i],end=" ")
                break
            else:
                print(l1[i]+l2[j],end=" ")
                break


