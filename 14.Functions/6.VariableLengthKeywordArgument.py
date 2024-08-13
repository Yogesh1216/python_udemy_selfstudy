# variable length arguments:
# variable length keyword arguments:
# mixed arguments:


# variable length arguments:
def fun(*args):
    print(args)


fun(11,22,33,44,55,66,77)

# variable length keyword arguments:
def fun(**kwargs):
    print(kwargs)


fun(a=11,b=22,c=33,d=44)

# mixed arguments:
def fun(a,b,*args,c,**kwargs):    #args will get values in tuple and kwargs in dictionary.
    print(a,b,args,c,kwargs)


fun(1,2,11,22,33,c=1,num1=10,num2=20,num3=30)

