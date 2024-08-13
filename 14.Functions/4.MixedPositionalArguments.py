
def add(a,b,/,c,d,e,f):
    return a+b+c+d+e+f

total = add(1,2,3,4,5,6)
print(total)
# total = add(d=1,a=3,b=2,c=4,e=6,f=5)
# print(total)

# restricting positional arguments / - a,b should be positional arguments only.
total = add(1,2,d=3,c=4,e=5,f=4)   #we connot write a=1,b=2 now as we have made them positional arguments.
print(total)                             # rest we can make positional or keyword arguments.


# a,b = must be positional | c,d = positional or keyword | e,f = must be keyword arguments.
def add1(a,b,/,c,d,*,e,f):
    return a+b+c+d+e+f


total = add1(2,3,2,d=5,e=1,f=5)




