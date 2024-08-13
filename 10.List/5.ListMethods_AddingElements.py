# adding elements : append() | extend() | insert() | copy()

# append() - adding one element at the end of the list:
list1 = [1,2,3,4,5]
list1.append(6)
print(list1)

# append using slicing:-
# list1[5:5] = [6]   # or
# list1[5:] = [6]    # or
list1[len(list1):]=[6]
print(list1)


# extend() - adding multiple elements:  you can use list , tuple,string --- iterables in extend(iterable)
list1 = [1,2,3]
list1.extend([8,9,10])
print(list1)

list1.extend('abc')
print(list1)    # [1, 2, 3, 8, 9, 10, 'a', 'b', 'c']

# extend using slicing
list1 = [1,2,3]
list1[len(list1):] = [6,7,8]
print(list1)

# insert(i,x) - inserting any element at a given index , i=index , x=data
list1 = [1,2,3]
list1.insert(0,10)      # [10, 1, 2, 3]
print(list1)  # it will insert 10 at index 0 and rest elements will shift to right

# insert using slicing
list1=[1,2,3]
list1[1:1] = [11]  # [1, 11, 2, 3]
print(list1)


# copy() = creates a shallow copy of list
l1= [1,2,3]
l2 = l1.copy()
print(l1)
print(l2)





