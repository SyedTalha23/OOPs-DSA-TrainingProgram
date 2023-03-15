start=int(input())
end=int(input())
arr=[i for i in range(start,end+1)]
print(arr)
subarr=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        subarr.append(arr[i:j+1])
print(subarr)
#subarr=[arr[i:j+1] for i in range(len(arr))] ==> list comprehension version
