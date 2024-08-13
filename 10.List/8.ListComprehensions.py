# ways to create list
list1 = []
for x in range(0,10):
    list1.append(x)
print(list1)

# l1 = [expression for item in iterable]
l1 = [x for x in range(0,10)]
print(l1)

l2 = [x**2 for x in range(0,5)]
print(l2)

l3 = [x for x in (10,5,7,12,3) if x%2==0]
print(l3)

l4 = [x.lower() for x in 'Python']
print(l4)

l5 = [x for x in 'ab12de-*&abfd343' if x.isalpha()]
print(l5)


names = input('enter your names: ')
l1 = names.split()
print(l1)

name = input('enter names').split()
print(name)


