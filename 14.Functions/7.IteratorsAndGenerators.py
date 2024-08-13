# iterators
L1 = [1,2,3,4,5]
t1 = (1,2,3,4,5)
str1 = 'abcde'
set1 = {1,2,3,4,5}
dict1 = {1:'A',2:'B',3:'C',4:'D',5:'E'}   # it will only print keys

print('List')
itr = iter(L1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print('Tuple')
itr = iter(t1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print('String')
itr = iter(str1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print('set')
itr = iter(set1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print('Dictionary')
itr = iter(dict1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


# Generators:
def Days():
    weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    i = 0
    while True:
        x = weekdays[i]
        i = (i+1)%7
        yield x          # this will not break the loop like return but will continue by maintaining value of i.

d = Days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

