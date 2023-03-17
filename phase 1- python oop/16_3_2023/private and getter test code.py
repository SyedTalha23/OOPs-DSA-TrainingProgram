class example:
    __num=99
    def __init__(self):
        self.__val=100
    def getter1(self):
        return self.__val
    def getter2(self):
        return example.__num

e=example()

print(e.getter1())
print(e.getter2())