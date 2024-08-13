# concat = list can be concatinated with list only

list1 = [1,2,3]
list2 = [8,9,10]
print(list1+list2)

print(list1+[4])  # list added with list

# updating existing list:
list1.extend([4,5,6])
print(list1)

# repetation  *
print(list1*2)

# in and not in = returns boolean
list1 = [1,2,3]
if 1 in list1:
    print('True')

if 1 not in list1:
    print('False')





