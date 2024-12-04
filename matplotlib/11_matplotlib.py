# How to add data value in the bar or line graph using python matplotlib

'''import matplotlib.pyplot as plt
import numpy as np

categories = ['Category 1', 'Catogery 2', 'Category 3']
Values = [20,35,40]

# Create a bar plot

plt.bar(categories, Values)

for i, value in enumerate(Values):      # doing marking
    plt.text(i, value+1, str(value), ha = 'center', va = 'bottom')

plt.show()'''


# Creating line graph

import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [10,25,13,32,20]
plt.plot(x_values,y_values, marker='o')

for x,y in zip(x_values, y_values):
    plt.text(x, y +1, str(y), ha='center', va='bottom')

plt.show()