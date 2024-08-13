# Build in function
# abs() = convert -ve values to +ve values:-
num1 = -15
print(abs(num1))

#ascii() = to find ascii code of any letter or number:
# bin() = convert to binary
#bool() = convert to bool datatype
# bytes() = convert array of bytes

#enumerate() = adds indexing to a list
#eval() = evaluate expression
print(eval('3*10+9'))

#---------------------------------
# filter()
list1 = [3,6,7,9,12,14,19,21]
def even(x):
    if x%2==0:
        return True
    else:
        return False

f = filter(even,list1)

for i in f:
    print(i)

#
f = filter(lambda x:x>10,list1)
for i in f:
    print(i)


# frozenSet()

#map()
list1 = [1,2,3,4,5]
m = map(lambda x:x**2,list1)
for i in m:
    print(i)

# sorted(L1)
# sorted(L1,reverse=True)   = it will create a new list.
#slice()
# zip()

# reversed()   , it works same as iter() iterator but in reverse order.
# pow(2,4)   will be 16
# round()
r=round(12.26)
print(r)
