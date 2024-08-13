# for | for using range | while loop

list1 = [5,6,7,8,9]
for i in list1:
    print(i)


for i in range(0,len(list1)):
    print(list1[i])


# reverse
for i in range(len(list1)-1,-1,-1):
    print(list1[i])

# reverse using -ve index
for i in range(-1,-len(list1)-1,-1):
    print(list1[i])

# while loop
i = 0
while i< len(list1):
    print(list1[i])
    i +=1




