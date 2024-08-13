# Area of triangle = 1/2*b*h
base = int(input('Enter the length of base of triangle: '))
height = int(input('Enter the length of height of triangle'))
area = 1/2*base*height
print('Area of triangle is: ',area)

# Area of Rombus:- 1/2*(a+b)*h
side1 = int(input('Enter the length of 1st side of rombus: '))
side2 = int(input('Enter the length of 2nd side of rombus: '))
height = int(input('Enter the height of rombus: '))
area = float(1/2*(side1 + side2)*height)
print('Area of Rombus is: ',area)

# displacement = v2-u2/2a
finalVelocity = int(input('Enter the initial velocity'))
initialVelovity = int(input('Enter the final velocity'))
accelration = int(input('Enter the value of acceleration'))
area = (finalVelocity**2-initialVelovity**2)/(2*accelration)


