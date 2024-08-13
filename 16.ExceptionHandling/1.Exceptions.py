# Types of error :-
# syntax error | logic error | runtime error

list1 = [12,13,42,56]
n = int(input('Enter the index'))
try:
    print(list1[n])
except:
    print('Invalid index- index out of range')


num1 = 10
num2 = 0
try:
    print(10/0)
except (ValueError,ZeroDivisionError) as error:
    print(f'Error:{error}')
