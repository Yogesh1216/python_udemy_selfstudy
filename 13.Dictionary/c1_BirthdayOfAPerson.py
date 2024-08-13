#find birthday of a person:
birthdays={
    'Sachin':'03/14/2003',
    'Carl':'01/17/2001',
    'Khan':'12/10/2006',
    'Donald':'06/14/2010',
    'Rohan':'01/06/2005'
}

name = input('give your name to find your birthday: ')
print(f'{birthdays.get(name,'name is not found')}')


if name in birthdays:
    print(birthdays[name])
else:
    print('name not found')