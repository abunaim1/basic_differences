"""
Operator overloading means when we use a operator with a user defined methode, its called operator overloading. 
For example:
"""
class Person:
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    def __gt__(self, other):
        return self.age > other.age
    def exersize(self):
        raise NotImplementedError
        print('Not mandatory for all person')

p1 = Person('Sakib', 22, 'Dhaka')
p2 = Person('Mahdfuz', 23, 'Cumilla')

if p1>p2:
    print('Sakib Buro')

else:
    print('Mahfuz Buro')


"""
Operator overriding means when we re-use a methode that already declared in other class called operator overriding.
For example:
"""
class Swimmer(Person):
    def __init__(self, name, age, address) -> None:
        super().__init__(name, age, address)
    def exersize(self):
        print('Manadory Exersize')

s1 = Swimmer('Atik', 22, 'chipa')
print(s1.exersize()) # this exersize method overrride from person class. 
