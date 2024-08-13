# AP
initial_value= int(input('Enter initial value: '))
difference = int(input('Enter the difference: '))
terms = int(input('How many terms you want to print: '))
for i in range(initial_value,terms*difference+initial_value,difference):
    print(i)

# Fibonacci  0,1,1,2,3,5,8,13.....
num = int(input('How many no. you want o print of fibonacci: '))
a = 0
b = 1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c


