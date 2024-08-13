# acquiring features of existing class into new class

# Reusablity of code.

class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth

    def parameter(self):
        return 2*(self.length+self.breadth)

class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height = h
        super().__init__(l,b)     # this is way to send params to parent class constructor.
        # 1st way is by using super , 2nd way by initializing parent class properties in child class
        self.length=l
        self.breadth=b

    def volume(self):
        return self.length*self.breadth*self.height



obj1 = Rectangle(5,6)
print(obj1.area())

# obj2 = Cuboid(10)
# print(obj2.volume())

# when we create a object of child class , constructor of parent class is not called.
obj3 = Cuboid(5,2,10)
print(obj3.volume())
print(obj3.area())





