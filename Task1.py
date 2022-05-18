# A program that reads a csv file and displays on the screen
import csv
import pandas as pd


file_name = pd.read_csv('datapoints.csv')
list_data = file_name
print( list_data.head())