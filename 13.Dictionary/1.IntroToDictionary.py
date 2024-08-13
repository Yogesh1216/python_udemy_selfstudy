# Dictionary : key value pairs...
dict1 = {'abacus': 'a calculator','bachelor': 'unmarried person', 'cable': 'strong wire'}
print(dict1['abacus'])

# datatype for key :- immutable type like int ,string  value : any datatype

dict2 = {101: 'John', 102: 'Smith', 103: 'Mark',104: 'David'}
# access | insert | update | delete

print(dict2[101])   #access
dict2[101]='yogesh' #update
print(dict2[101])
dict2[105]='ajay'   #insert
print(dict2)
del dict2[104]      #delete
print(dict2)

# traveresing all data of dictionary
for i in dict2:
    print(i)     # it will print all the keys

for i in dict2:
    print(i,dict2[i])   # it will print all the key and values.



