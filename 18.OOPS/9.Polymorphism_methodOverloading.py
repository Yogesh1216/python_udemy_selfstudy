class Yogesh:
    def sum(self,a,b):
        print(a+b)

y = Yogesh()
y.sum(3,4)
y.sum('Hello ','Yogesh')
y.sum(3.4,6.3)


class A:
    # def sum(self,a,b):   # this will shaddow.
    #     print(a+b)
    def sum(self,a,b,c=None):   # we can modify in this way
        sum = a+b
        if c == None:
            print(sum)
        else:
            print(a+b+c)

obj1 = A()
obj1.sum(2,3)
obj1.sum(2,3,4)
# NOTE : when we call a method of a function with same name , latest will be called , prev method will be shadowed.



