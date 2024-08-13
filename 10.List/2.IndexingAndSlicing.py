list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[0])
print(list1[-1])

# slicing   list1[start:end:step]
print(list1[:])
print(list1[0:10])
print(list1[0:10:2])
print(list1[1:10:2])

# reverse a list
print(list1[::-1])

# updating list using slice:
list1 = [1,2,3,4,5,6,7,8,9,10]
list1[0:3] = [10,20,30]
print(list1)     # [10, 20, 30, 4, 5, 6, 7, 8, 9, 10]

list1[0:3] = [10,20]
print(list1)    # [10, 20, 4, 5, 6, 7, 8, 9, 10]

list1[0:3] = [10,20,30,40,50]
print(list1)    # [10, 20, 30, 40, 50, 5, 6, 7, 8, 9, 10]

# if you want to update using steps than give all the steps of the list else it gives error: eg:-
list1 = [1,2,3,4,5,6,7,8,9,10]
list1[::2] = [11,33,55,77,99]
print(list1)     # [11, 2, 33, 4, 55, 6, 77, 8, 99, 10]





