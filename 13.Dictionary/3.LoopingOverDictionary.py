# looping through dictionary:
dict1 = {101:'Productoin',102:'Accounts',103:'Sales&Marketing',104:'Inventory'}
for i in dict1:
    print(i) # it will give the keys

for i in dict1:
    print(i,dict1[i])  # will return key and values

for i in dict1:
    print(i,dict1.get(i))

# difference between fetching value by dict1[i] and dict1.get(i)
#NOTE1 - if value does not exist
#print(dict1[106])   #it gives error
print(dict1.get(106))  #it will return none or some message we want to show.
print(dict1.get(106,'value does not exist'))

# get() | keys() | values() | items()
print(dict1.keys())
print(dict1.values())
print(dict1.items())

for i in dict1.keys():
    print(i,dict1[i])
for i in dict1.values():
    print(i)
for x,y in dict1.items():
    print(x,y)