#Counting the number of digits in a number
num = int(input('Enter a Number: '))
length = 0
while num>0:
    num = num//10
    length += 1
print(length)

# Find the sum of digits in a number:
num1 = int(input('Enter a number: '))
sum = 0
while num1>0:
    r = num1%10
    num1 = num1//10
    sum +=r
print(f'Sum is {sum}')

# Reverse a Number:
num1 = int(input('Enter a number: '))
i=0
while num1>0:
    r = num1%10
    num1 = num1//10
    i = i*10+r
print(i)

    # re = str(r)
    # rev +=re
#print(rev)

# Num is palindrome or not:
num = int(input('Enter a Number: '))
copyNum = num
rev=0
while num>0:
    r = num%10
    rev = rev*10+r
    num = num//10
if copyNum==rev:
    print('Its a palindrome')
else:
    print('Not a palindrome')