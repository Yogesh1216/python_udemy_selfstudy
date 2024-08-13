# variable length argument - can pass as many arguments we want.
# unpacking arguments
# multiple return values

def fun(*args):
    print(type(args),args)
# it will give type as tuple.

fun()
fun(10,20)
fun(10,20,30,40,50,60,70,80,90,100)
fun(10,'Hello',24.75,True)


def fun1(a,b,*args):
    print(a,b,args)


# fun1()  - error (its compulsory to pass 2 arguments a,b now and these should be positional arguments )
fun1(10,20)
fun1(10,20,30,40,50)

# we can also write keyword arguments at the end in such way
def fun2(*args,a,b):
    print(args,a,b)


# fun1()  - error (its compulsory to pass 2 arguments a,b now and these should be positional arguments )
fun2(a=10,b=20)
fun2(10,20,30,a=40,b=50)



# unpacking arguments
def fun3(a,b,c):
    print(a,b,c)

L1 = [11,22,33]
tuple1 = (10,20,30)
str1 = 'sky'
set1={21,55,12}  # its order will be different
fun3(L1[0],L1[1],L1[2])  #OR
fun3(*L1)  # we can use * - it will pass list as individual arguments
fun3(*tuple1)
fun3(*str1)
fun3(*set1)


# multiple return values
def calculate(a,b):
    sum = a+b
    difference = a-b
    multiply = a*b
    divide = a/b
    return sum,difference,multiply,divide


sum,difference,multiply,divide = calculate(30,2)
print(f'Total:{sum}, difference:{difference}, multiply:{multiply}, divide:{divide}')

t= calculate(30,2)
print(type(t),t)    # t will be a tuple have all return



