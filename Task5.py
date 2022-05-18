# A program that finds a value for a that gives the lowest 
#possible MSE
import numpy as np
import pandas as pd
import csv

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

for x in list_data['x']:
    y_true.append(a * x + b)


#Calculating the MSE using the formula 1/N∑(Y-Ytrue)**2 
MSE = np.sum(np.subtract(y,y_true)**2)/n   

i = 1
while i < 100:
    new_y_true = []
    new_MSE = 0
    a = a - 0.1
    for x in list_data['x']:
        new_y_true.append(a * x + b)

        #Recalculate MSE
    new_MSE = np.sum(np.subtract(y,new_y_true)**2)/n

    #checking to see if the new_MSE is smaller than previous MSE
    if new_MSE < MSE:
      MSE = new_MSE
    i += 1

print('A value for a that gives the lowest possible  MSE is ', 'a = ', a, '\t' 'MSE = ', MSE, '\n')

        
