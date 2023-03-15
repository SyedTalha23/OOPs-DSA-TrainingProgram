class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
person = Person("John", 30)
print(person)  # output: John is 30 years old
