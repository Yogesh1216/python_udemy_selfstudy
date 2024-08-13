# declare variables
a = 10
b = 12.9

name = 'yogesh'
x,y,z = 5,10,15
print(x,y,z)

u=v=w=1
print(u)

# python is dynamically typed language:
x = 25
print(type(x))
x = 13.75
print(type(x))
x = 'A'
print(type(x))
x = [1,2,3,4]
print(type(x))
x = True
print(type(x))
# everything in python is object
#( changing datatype from int ->float->string)


# rules for declaring names:
    # name can contain alphabets and numbers. eg - x1,address1
    # name should start with letter or underscore
    # name of variable should be definable
    # keyword should not be used.
    # variable are case-sensitive.


# datatypes:
  # 1) numeric - int float , bool, complex
  # 2) sequence - list(values can be changed) , tuple(values cannot be changed) , string , bytes (0-255), bytearray(0-255)   (in sequence every value has its index)
  # 3) set - set , frozenset (set values are not index based)
  #4) dictionary - dict (key-value pairs)

# there is no fix size limit for variable in python .
x = 50234325235325235;
print('size is :',x.__sizeof__())
x1 = 12.3434
print(x1)
# bool - used for true false conditions:
if(x>x1):
    print('true')

# complex - real+imagionary  = a+jb  where j= underroot -1
x2 = 1+3.55j
print(type(x2))
print(x2)
print(x2.real)
print(x2.imag)





