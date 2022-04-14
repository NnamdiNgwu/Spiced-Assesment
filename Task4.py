# this Program Calculates the Mean Squared Error (MSE) of y and ytrue from the datapoints csv file
# using the formula:MSE = 1/N∑(y−ytrue)2

import numpy as np
import csv

with open("datapoints.csv", newline='') as file_name:
 readData = csv.reader(file_name)
 listData = list(readData)
 listData.pop(0)

# Given Value
y = [float(row[1]) for row in listData]

# Approximated Value
y_true = [round(float(row[1])) for row in listData]

# Calculation of Mean Squared Error (MSE)
MSE = np.square(np.subtract(y_true, y)).mean()
print(MSE)