# startswith | endswith | removesuffix | removeprefix | partition | rpartition

s = 'python is very easy'

# startswith(prefix[,start[,end]])
print(s.startswith('python'))
print(s.startswith('py'))
print(s.startswith('is',7))

# startswith(prefix[,start[,end]])
print(s.endswith('easy'))
print(s.endswith('is',0,9))

# removesuffix
print(s.removeprefix('py'))

# removesuffix
print(s.removesuffix('sy'))

# partition - creates 3 parts.
print(s.partition('is'))
print(s.partition(' '))

# rpartition
print(s.rpartition('e'))




