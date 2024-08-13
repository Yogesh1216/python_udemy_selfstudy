# index() | count() | reverse() | sort()

# index(x[,starat][,end])  = used to search element and return index.
# if element is not found it gives error.
list1 = [5,6,7,5,8,9,6,10,6]
print(list1.index(8))
print(list1.index(6,2,7))


# count() - how many times value is repeating
list1 = [5,6,7,5,8,9,6,10,6]
print(list1.count(6))

# reverse() - reverse a list
list1 = [1,2,3,4]
list1.reverse()
print(list1)

# sort(*,key=None,reverse=False)
list1 = [5,6,7,5,8,9,6,10,6]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1 = ['yy','jj','BB','aa','ZZ']
list1.sort()
print(list1)    # ['BB', 'ZZ', 'aa', 'jj', 'yy']

list1.sort(key=str.lower)
print(list1)    # ['aa', 'BB', 'jj', 'yy', 'ZZ']

# sorted() - this will not modify the original list , it will create a copy .
sorted(list1)    # ['aa', 'BB', 'jj', 'yy', 'ZZ']








