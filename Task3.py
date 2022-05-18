#Set the slope a to 10 and the intercept b to 0. Calculate y 
# for every value of x.

import csv
import pandas as pd
import numpy as np

file_name = pd.read_csv('datapoints.csv')
list_data = file_name
list_data.head()
 
a = 10 
b = 0
for row in list_data:
    x = list_data['x']
    y = a * x + b

print('y = ' + str(y))
  




