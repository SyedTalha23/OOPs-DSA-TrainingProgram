def check_double(n):
    d=2*n
    s1=str(n)
    s2=str(d)
    count=0
    if len(s1) == len(s2):
        for i in s1:
            for j in s2:
                if i==j:
                    count+=1
        if count==len(s1):
            return True
    return False
print(check_double(125874))
print(check_double(128574))
print(check_double(142587))
print(check_double(142857))
print(check_double(12))

