# isupper | islower | istitle
# all returns true or false

s = "HELLO"
print(s.isupper())

s = 'Hello'
print(s.islower())  # False

s = 'How Are You'
print(s.istitle())  # True

# isalnum | isalpha | isspace
s1 = 'abc123'
print(s1.isalnum())  # True   - contain alphabet and numeric(if special character it will return false)
print(s1.isalpha())  # False checks if string only contains alphabets.
print(s.isspace())  # check if string contain space
print(s1.isascii())  # if all numbers are in ascii code.

# isidentifier | isprintable | isdecimal | isdigit | isnumeric
s1 = 'length1'
print(s1.isidentifier())  # gives true if it contains valid name for variable
s1 = 'hello \n how r u'
print(s1.isprintable())  # if it contains non-printable data than it will return false.

num1 = '123.1'
print(num1.isdecimal())  # gives false for decimal values
# num1 = 2 power 2 it returns true for isdigit() but false for isdecimal()

# isnumeric = 2 power 1/2 - gives false for isdecimal() and isdigit()but true for isnumeric
