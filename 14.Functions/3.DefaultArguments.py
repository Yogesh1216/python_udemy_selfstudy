# Default Arguments:-
# 1. Default arguments should be on the right side.
# 2. keyword argument should be in right side.
# 3. Defaults are created only once.
def add(a,b=0,c=0):
    sum = a+b+c
    return sum


total = add(3,5,4)
print(total)
total = add(3,5)
print(total)
total = add(3,b=2)
print(total)


def addition(item , L=[]):
    L.append(item)
    return L


# it keeps on adding in the same list
list = addition(22)
print(list)
list = addition(33)
print(list)

