def func(s):
    if len(s)<3:
        return s
    elif s[-3:]=="ing":
        return s+"ly"
    else:
        return s+"ing"

print(func("sleep"))
print(func("amazing"))
print(func("is"))

