# marks should be between 0-100
marks = int(input('enter your marks: '))
if marks >= 0 and marks <= 100:
    print('your marks are valid')
else:
    print('Please enter valid marks')

#check if a person is male or female:-
gender = input("enter your gender 'm' or 'M': ")
if gender=='M' or gender=='m':
    print('you are male')
elif gender=='f' or gender=='F':
    print('you are female')
else:
    print('Invalid type')

# check if person is eligible to work of not:
age = int(input('enter your age: '))
if age < 18 and age < 60:
    print('you are not eligible to work')
else:
    print('you are not eligible to work')

