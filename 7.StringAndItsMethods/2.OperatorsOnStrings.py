# Concatination  | Repetition | Indexing | Slicing | in | not in

# Concatination
s1 = "Hello"
s2 = "World"
s3 = s1+s2
print(s3)

s4 = "Hello" "World"
#s5 = "Hello" +15   # we need to convert int type to string to concat
s5 = "Hello" + str(15)
print(s5)


#Repetition
s1= "hi"
print(s1*3)

# Indexing
string1 = "Hello World"   #11
print(string1[2])
print(string1[-10])

for x in string1:
    print(x)
#or
for i in range(0,len(string1)):
    print(string1[i])

# printing using reverse index
for i in range(len(string1)-1,-1,-1):
    print(string1[i])


# Slicing:-   s1[start:end:step]
s1 = "yogesh"
print(s1[0:len(s1):1])
print(s1[:len(s1):1])
print(s1[::1])
print(s1[::])     #yogesh
print(s1[3::])    #esh
print(s1[3:5])    #es
print(s1[::2])    #ygs
print(s1[::-1])   #hsegoy
print(s1[-1:-len(s1)-1:-1])

if 'o' in s1:
    print(True)

if 'o' not in s1:
    print(False)






