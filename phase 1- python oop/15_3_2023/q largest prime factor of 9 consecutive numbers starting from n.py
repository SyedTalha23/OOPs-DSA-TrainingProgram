n=int(input())
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def hprime(n):
    temp=n
    while(temp>0):
        if n%temp==0:
            if isprime(temp):
                return temp
        temp-=1

sum=0
for i in range(n,n+9):
    sum=sum+hprime(i)
print(sum)

