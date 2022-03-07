"""
Write a Python program to read specific columns of a given CSV file and print the content
of the columns.

"""
import csv


colum_name=input("Enter Column name:")

with open('username.csv','r') as csvf:
    data=csv.DictReader(csvf,delimiter=";")
    print("conten of "+colum_name+" is ")
    for row in data:
        print(row[colum_name])


