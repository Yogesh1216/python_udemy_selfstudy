
# global variable can be accessing in the function
g=10
def fun1(a):
    l=a
    print(g)   # global variable is accessed
    print(l)

fun1(1)



def fun2(a):
    l = a

g=11
fun2(2)
print(g)
#print(l)   #local variable can be accessed only within function.


# if we use global in local scope.
g = 10
def fun3(a):
    g = a
    print(g)     # 1   (it will access local variable)

fun3(1)
print(g)    # 10   (it will access global variable)


# NOTE: a functon can access global variable but cannot modify them
g=10
def fun4(a):
   # g = g+2  #error
    print(g)

fun4(1)

# modifying global variable:
g=10
def fun5():
    global g
    g = g+2
    print(g)  #12

fun5()
print(g)   #12


# locals() = gives all the local variables in the form of dictionary and globals()= give all global variables.
a,b,c,d,e = 1,2,3,4,5
def fun5(l=5,m=4):
    x,y,z = 10,20,30
    print(locals())     # {'l': 5, 'm': 4, 'x': 10, 'y': 20, 'z': 30}

fun5()
print(globals())






