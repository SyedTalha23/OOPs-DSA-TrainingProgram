def func(string):
    if len(string)<2:
        return -1
    else:
        #s=string[0:2]+string[len(string)-2:len(string)]
        s=string[0:2]+string[-2:]
        return s

print(func("w3resource"))
print(func("w3"))
print(func("A"))