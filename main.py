# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


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

