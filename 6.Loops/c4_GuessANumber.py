# guess a no from 1-10
import random

randomNumber = random.randint(1,10)
userInput = 0
while randomNumber!=userInput:
    userInput = int(input('Enter a no. : '))
    if userInput>randomNumber:
        print('You entered a larger no.')
    elif userInput<randomNumber:
        print('You entered a smaller no.')
    else:
        print('You got your number')