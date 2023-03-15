def find_pair_of_numbers(l,n):
    count=0
    i=0
    while(i<len(l)):
        j=i+1
        while(j<len(l)):
            if (l[i]+l[j])==n:
                count+=1
            j+=1
        i+=1
    print(count)

find_pair_of_numbers([1,2,7,4,5,6,0,3],6)
find_pair_of_numbers([3,4,1,8,5,9,0,6],9)