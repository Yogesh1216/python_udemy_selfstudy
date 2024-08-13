# replace | join | split | rsplit | splitlines |

s = 'a-b-c-d-e'
print(s.replace('-',','))
print(s.replace('-',',',3))   # count is optional.

# join
s1 = 'xyz'
s2 = 'abc'
print(s1.join(s2))   # axyzbxyzc

s1 = '/'
s2 = 'abc'
print(s1.join(s2))   # a/b/c   s1 act as seperator for s2.

l1 = ['john','smith','ajay']
s1 = ','
print(s1.join(l1))   # john,smith,ajay

# split
s = 'john smith ajay'
print(s.split())       # ['john', 'smith', 'ajay']

s = 'john,smith,ajay'
print(s.split(','))    # ['john', 'smith', 'ajay']
print(s.split(',',1))  # ['john', 'smith,ajay']


s = 'john,smith,ajay'
print(s.rsplit(',',1))

# splitlines
s = 'aaa\nbbb\tccc\rddd/feee'
print(s.splitlines())   # ['aaa', 'bbb\tccc', 'ddd/feee']
print(s.splitlines(keepends=True))    # ['aaa\n', 'bbb\tccc\r', 'ddd/feee']


