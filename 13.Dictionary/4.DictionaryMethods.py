original_config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'credentials': {
            'username': 'user',
            'password': 'pass'
        }
    },
    'features': ['feature1', 'feature2', 'feature3'],
    'data': 1
}

# copy() , update(), setdefault(),fromkeys()

#deepcopy is clone of whole data - changing in this will not impact orignal data.
import copy
deepcopyData=copy.deepcopy(original_config)
deepcopyData['data']=12
print(original_config)
print(deepcopyData)


# copy() creates a shallow copy of object.  this will refer to same key values of object1
# .it will not create its own copy  -- it will change nested data
modifiedConfigShallowCopy = original_config.copy()
modifiedConfigShallowCopy['data']=5
modifiedConfigShallowCopy['database']['port']=8080

print(original_config)
print(modifiedConfigShallowCopy)

#update()   # you can add multiple records in one go like this.
dict1 = {101:'Productoin',102:'Accounts',103:'Sales&Marketing',104:'Inventory'}
dict2 = {105:'IT',106:'CSE'}
dict1.update(dict2)
print(dict1)
dict1.update({101:'Productoin1'})
print(dict1)

#setdefault()  # this will work as .get() method | if value id not there get() returns none but setDefault() makes a new entry.
print(dict1.setdefault(101))
dict1.setdefault(110)        #110: None
dict1.setdefault(111,'ECE')  #111: 'ECE'
print(dict1)

#fromkeys()   key values with same value.
dict2= [1,2,3,4]
dict1.fromkeys(dict2,'a')

# deleting = pop(key,default) | popitem() | clear()
dict1 = {101:'Productoin',102:'Accounts',103:'Sales&Marketing',104:'Inventory'}
dict1.pop(104)
#dict1.pop(114)  #error - 114 does not exist
dict1.pop(114,'key not found')
print(dict1)

dict1.popitem()    #remove last data.
print(dict1)

dict1.clear()  # it will clear data of full dictionary.
print(dict1)
