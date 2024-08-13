# capitalize() | lower()  upper()  | title()  | swapcase()  |  casefold()

s1 = 'hello dear'
print(s1.capitalize())

s1 = 'HELLO how Are YOu'   # will keep only 1st letter capital rest as small
print(s1.capitalize())    # Hello jow are you

print(s1.lower())    #hello how are you
print(s1.upper())    #HELLO HOW ARE YOU
print(s1.swapcase()) #hello HOW aRE yoU
print(s1.title())    #Hello How Are You
print(s1.casefold())  # work as same to lower() but casefold() is used for unicode eg-german language to lower case.

# its better to use casefold() instead of lower() for conditional statements.








