# ljust() | rjust() | center  = all used for text allignment.
s = 'python'
print(s.ljust(10))
print(s.rjust(10))
print(s.center(10))

print(s.ljust(10,'-'))
print(s.rjust(10,'+'))
print(s.center(10,'*'))


# to remove extra spaces - lstrip() , rstrip() , strip()
s1 = '   python    '
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())  #Removed extra spaces.

s1 = '.... ..yogesh+++++'
print(s1.lstrip('.'))

s1 = '.... ..yogesh+++++'
print(s1.lstrip('. +'))





