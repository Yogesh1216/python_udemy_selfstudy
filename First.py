# num = int(input('Enter a number : '))
# fact = 1
# for i in range(1,num+1):
#     fact = i*fact
#
# print(fact)


# num = input('enter a no: ')
# # removeDigits =1 # int(input('How many digits you want to remove : '))
# # redefinedNo=0
# for i in num:
#     num = num//10



import numpy as np
from numpy import random
import matplotlib.pyplot as plt
base_array = np.array([15,58,64,25,65,25,145,24,28,36])
plt.show()
new_array = base_array.reshape(2,5,-1)
def my_add(n1, n2):
  return n1+n2
my_add = np.frompyfunc(my_add, 2, 1)
arr = np.arange(1, 11)
while(arr.all()!=0):
    for num in range (base_array):
       print(my_add)
my_add(15,10)
