"""
Write a Python program to read a file line by line and store it into a list.

"""

with open("sample.txt",'r') as file:
    output=file.readlines()

print("Content of file is          :",output)