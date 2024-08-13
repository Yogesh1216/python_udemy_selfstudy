num = int(input('Enter a number: '))
for i in range(1,num+1):
    if num%i == 0:
        print(i)

# is number prime or not:
num = int(input('enter a mumber: '))
count = 0
for i in range(1,num):
    if num%i==0:
        count +=1
    elif count>=2:
        print('Not a prime n.')



