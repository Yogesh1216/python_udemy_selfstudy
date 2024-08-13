# pop() or del | remove() | clear()

# pop(i) - remove last element , if i is given then delete specified index
l1 = [1,2,3,4,5,6,7,8,9]
l1.pop()
print(l1)   # [1, 2, 3, 4, 5, 6, 7, 8]
l1.pop(0)
print(l1)   # [2, 3, 4, 5, 6, 7, 8]

del l1[0]
print(l1)   # [3, 4, 5, 6, 7, 8]

del l1[0:3]
print(l1)   # [6, 7, 8]

# remove() = will remove element 1st element
l1 = [1,2,3,4,5,5,6]
l1.remove(5)
print(l1)   # [1, 2, 3, 4, 5, 6]
# if value is not in list than it will give error.

# clear() = clear entire list
list1 = [1,2,3]
list1.clear()
print(list1)   # []

# or
list1 = [1,2,3]
del list1[:]
print(list1)   # []

