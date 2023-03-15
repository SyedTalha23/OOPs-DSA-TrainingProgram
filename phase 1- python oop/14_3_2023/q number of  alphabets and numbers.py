def func(string):
    countalpha=0
    countnum=0
    for i in string:
        if 'a'<= i<= 'z':
            countalpha+=1
        elif i >='A' and i<='Z':
            countalpha+=1
        elif i>='0' and i<='9':
            countnum+=1
    #print(list([countalpha,countnum])) it works too
    l=[countalpha,countnum]
    return l
print(func("infosys 123"))
#we can do it using str.isalpha() and str.isdigit() method too