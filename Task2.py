# this program creates a scatterplot of the data from datapoints.csv file

from cProfile import label
import csv
import matplotlib.pyplot as plt

with open("datapoints.csv", newline='') as file_name:
    readData = csv.reader(file_name)
    data = list(readData)
    data.pop(0)
  
    x = [x[0] for x in data]
    y = [x[1] for x in data]

    plt.scatter(x, y, label="point", color="b")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title = "Task 2 - Scattered Points"
    plt.legend()
    plt.show()