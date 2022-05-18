# this program creates a scatterplot of the data from datapoints.csv file

from cProfile import label
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_name = pd.read_csv('datapoints.csv')    
list_data = file_name
x = []
y = []
for x in list_data:
    x = list_data['x']
    y = list_data['y']

plt.scatter(x, y, label='points', color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title = 'Task 2 - Scattered Points'
plt.legend()
plt.show()