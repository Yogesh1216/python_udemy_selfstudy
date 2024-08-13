# converting one datatype to other datatype:

# implicit conversion | explicit conversion
# int() | float() | complex() | bool() | str()

i = 15
x = float(i)
print(type(x))
print((x))

x = complex(i)
print(type(x))
print((x))

x = bool(i)
print(type(x))
print((x))

x = str(i)
print(type(x))
print((x))

f= 16.59
x = int(f)
print(type(x))
print((x))

x = complex(f)
print(type(x))
print((x))

b = True
x = int(b)
print(type(x))
print((x))

x = float(b)
print(type(x))
print((x))

x = complex(b)
print(type(x))
print((x))

c = 10+6j

s = 'john'

s1= '123'
x = int(s1)
print(type(x))
print((x))

x = float(s1)
print(type(x))
print((x))

s2 = '12+3j'
x = complex(s2)
print(type(x))
print((x))

x = complex(10)
print(x)
x = complex(10,2)
print(x)

