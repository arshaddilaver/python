"""
Write a Python program to read each row from a given csv file and print a list of strings.


"""

import csv

with open('username.csv','r') as csvf:
    data=csv.reader(csvf,delimiter=";")
    for i in data:
        print(i)


