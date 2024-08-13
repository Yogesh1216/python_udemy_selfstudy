# find() | rfind() | index() | rindex() | count()

s = "hello, how are you"
result = s.find('o')
print(result)   # 4

# NOTE: start and end points are optional.
result = s.find('o',5,8)
print(result)    # -1   it returns -1 when there is not in this range.

result = s.find('how')
print(result)

# rfind()
result = s.rfind('o')
print(result)  #16

result = s.rfind('o',0,10)
print(result)   #8

# index() , rindex()
result = s.index('o')
print(result)  #4    (NOTE - it is same as find and rfind , in case of not finding the substring
                        # in string it returns error but find and rfind return -1.)

# count()  - count gives the no. of occurrence of the digit or word in string.
result = s.count('o')
print(result)  # 3



