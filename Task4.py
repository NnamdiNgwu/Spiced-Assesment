# A program that calculates the Mean Square error of y and y_true
# using the formula:MSE = 1/N∑(y−ytrue)**2

import numpy as np
import csv
import pandas as pd

#opening a csv file using pandas
file_name = pd.read_csv('datapoints.csv')
list_data = file_name
list_data.head()

#Given values
a = 10
b = 0
n = len(list_data)
y = list_data['y']
y_true = []
MSE = 0

for row in list_data:
    x = list_data['x']
    y_true = a * x + b

#Calculating the MSE using the formula 1/N∑(Y-Ytrue)**2
MSE = np.sum(np.subtract(y,y_true)**2)/n
print('MSE = ', MSE)