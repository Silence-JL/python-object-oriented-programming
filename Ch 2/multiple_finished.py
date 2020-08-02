# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

# list A and B as base classes, with a comma, this is how to inherit more thatn one class at same time
# when call a class or access a attribute, Python use method resolution order to look it up in the class
class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


# create the class and call showname()
c = C()
print(C.__mro__)
c.showprops()
