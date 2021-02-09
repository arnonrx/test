class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print('Hello my name is '+ self.name)

class Persons:
    def __init__(self, name, age):
        myObj.name = name
        myObj.age = age

    def myfunc(self):
        print('Hello my name is ...' + myObj.name)

p1 = Person('John', 36)
p1.myfunc()

p2 = Person('Arnon', 30)
p2.myfunc()

p2.name = 'Adam'
p2.myfunc()