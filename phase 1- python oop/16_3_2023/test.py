class abc:
    __val=100
    def get_val(self):
        return self.__val

obj=abc()
num=obj.get_val()
print(num)