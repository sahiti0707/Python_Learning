class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello ! My name is " + self.name)


p1 = Person("Sahiti", 13)
p1.myfunc()
