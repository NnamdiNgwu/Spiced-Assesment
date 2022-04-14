# A program that reads a csv file and displays on the screen
import csv

with open("datapoints.csv", newline='') as file_name:
    readData = csv.reader(file_name)
    listData = list(readData)
    print(listData)