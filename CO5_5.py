"""
5. Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
read the CSV file and display the content.
"""
import csv



csv_columns = ['id','c1', 'c2', 'c3', 'c4']

dict_data = {'id':['1', '2', '3'],
    'c1':[33, 25, 56],
    'c2':[35, 30, 30],
    'c3':[21, 40, 55],
    'c4':[71, 25, 55],
     }

with open('sample.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    for data in dict_data:
        writer.writerow(dict_data)

        
data = csv.DictReader(open('sample.csv'))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
   break



