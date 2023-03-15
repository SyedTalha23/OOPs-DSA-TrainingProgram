def find_more_than_average(t):
    avg=sum(t)/len(t)
    counter=0
    for i in t:
        if i>avg:
            counter+=1
    print("percentage=",(counter/len(t))*100)

def generate_frequncy(t):
    f=[]
    for i in range(0,26):
        f.append(t.count(i))
    return f

def sort_marks(t):
    t=list(t)
    t.sort()
    #t=sorted(t) ==> sorted works for any data type while sort is only for list
    return(t)

marks=(12,14,15,3,15,2,3,3,5,0)
find_more_than_average(marks)
for i in range(0,26):
    print(f"frequncy of marks {i} = {generate_frequncy(marks)[i]}")
print(f"sorted marks= {sort_marks(marks)}")