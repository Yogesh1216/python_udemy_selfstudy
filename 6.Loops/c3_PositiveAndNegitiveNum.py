# Find the sum of given numbers as input:
numbers = int(input('How many numbers you want to enter: '))
total = 0
while numbers>0:
    num1 = int(input(f'Enter a number : '))
    total +=num1
    numbers -=1
print(f'Sum of all numbers is {total}')

# find sum of +ve and -ve numbers separately:
num_of_num = int(input('How many numbers you want to sum: '))
count = 0
positiveSum = 0
negativeSum=0
while count<num_of_num:
    num = int(input('Enter a number: '))
    if num >0:
        positiveSum = positiveSum+num
    elif num<0:
        negativeSum = negativeSum+num
    else:
        print('Number should not be 0 , Enter Number Again! ')
        continue
    count +=1
print(f'Sum of positive numbers {positiveSum}')
print(f'Sum of negative numbers {negativeSum}')


# Find Maximum out of all numbers:
numOfNumbers = int(input('How many numbers you want to enter: '))
count=0
num = int(input('Enter a number: '))
biggestNum=num
while count<numOfNumbers-1:
    num = int(input('Enter a number: '))
    if num>biggestNum:
        biggestNum=num
        count +=1
    else:
        count+=1
print(f'Biggest number is: {biggestNum}')

# Convert Decimal no to binary no:  This will give issue with nos. having 0 at the end in binary eg =10 - 1010 give 101.
num = int(input('Enter a number to convert in binary: '))
biNo=0
while num>0:
    r = num%2
    biNo = biNo *10+r
    num = num//2

#reverse a no
BinaryNo=0
while biNo>0:
    r = biNo%10
    BinaryNo = BinaryNo*10+r
    biNo = biNo//10
print(BinaryNo)


num = int(input('Enter a number to convert in binary: '))
biNo=''
while num>0:
    r = num%2
    biNo = str(r)+biNo
    num = num//2
print(biNo)












