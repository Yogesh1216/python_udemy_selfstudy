# leap year =      a year divisible by 100  -div by 400 (leap) | not divisible by 400 (not leap)
# divisible by 100 and 4 = its leap year
year = int(input('enter the year : '))
if year %100==0 and year %400==0:
    print(f'{year} is leapyear')
if year %100==0 and year %400!=0:
    print(f'{year} is not a leapyear')
if year%4 ==0:
    print(f'{year} is leapyear')

    

