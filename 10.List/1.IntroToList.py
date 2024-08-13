# list creation

list1 = list((1,2,3,4,5))
print(list1)

list2 = [1,2,3,4,5,6]
print(list2)

# accessing elements from list:
print(list1[2])
print(list2[-1])

# list is hetrogeneous - you can use multiple data type objects in list
myList = ['john',15,14.6,True,'steven',5+7j]
print(myList)

# list is mutable - list can be changed
mylist = [15,9,12,18,7,10]
mylist[0]=30    #updating
print(mylist)

print(len(mylist))

# adding to list
mylist.append(50)
print(mylist)


