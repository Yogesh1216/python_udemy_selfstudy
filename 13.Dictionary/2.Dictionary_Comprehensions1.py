# creating empty dictionary and filling data in it:
# way1:-
dict1 = dict()
dict1['name']='yogesh'
dict1['rollNo']='14'
print(dict1)

# way 2:-
dict2 = {}
for i in range(1,6):
    dict2[i]=i**2
print(dict2)

#------------dict2 = dict(iterable pairs)----------------
tuple1 = ((1,2),(3,4),(5,6))
dict1 = dict(tuple1)
print(dict1)

list1 = [(1,2),(3,4),(5,6)]
dict1 = dict(list1)
print(dict1)

tuple1 = ([11,22],[33,44],[55,66])
dict1 = dict(tuple1)
print(dict1)

string1 = ['ab','cd','ef']
dict1 = dict(string1)
print(dict1)

#------using zip function--------
list1 = [1,2,3,4]
list2 = ['apple','orange','gavava','banana']
dict1 = dict(zip(list1,list2))
print(dict1)

set1 = {7,8,9}    #set does not have any index so data will not come in order
str1 = 'AJK'
dict1 = dict(zip(set1,str1))
print(dict1)    #{8: 'A', 9: 'J', 7: 'K'}

# NOTE - IF THERE ARE EXTRA VALUES THEN THEY WILL BE IGNORED.
dict1 = dict(zip([10,20,30],(101,102,103,104,105)))
print(dict1)   #{10: 101, 20: 102, 30: 103}

#-------using enumerate function----------
list1 = ['A','B','C','D']
dict1 = dict(enumerate(list1))
print(dict1)  #{0: 'A', 1: 'B', 2: 'C', 3: 'D'}

for i in enumerate(list1):
    print(i)    # enumerate convert each element in set starting with 0  -  (0, 'A')

#
dict6 = {x:x**2 for x in range(1,5)}
print(dict6)   #{1: 1, 2: 4, 3: 9, 4: 16}

dict7 = dict((x,x**2) for x in range(1,5))
print(dict7)    #{1: 1, 2: 4, 3: 9, 4: 16}

list1 = [1,2,3,4]
list2= 'abcd'
dict8 = dict((x,y) for x,y in zip(list1,list2))
print(dict8)   #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

dict8 = {x:y for x,y in zip(list1,list2)}
print(dict8)

dict9 = {x:y for x,y in enumerate(list2)}
print(dict9)  #{0: 'a', 1: 'b', 2: 'c', 3: 'd'}

dict9 = dict((x,y) for x,y in enumerate(list2))
print(dict9)  #{0: 'a', 1: 'b', 2: 'c', 3: 'd'}


for x,y in zip(list1,list2):
    print(x,y)
# we can use in 2 ways -  1st  x:y   2nd (x,y)


