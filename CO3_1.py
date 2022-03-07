#Rahul
#21mca035

import os 
import sys

print("Working with OS package")
print("Current working directory is",os.getcwd())
print("List of Directories and files in current folder ",os.listdir())

print("____________________________________________________________________")

print("Working with Sys Package")

a=10
print("Size of object a is {} bytes ".format(sys.getsizeof(a)))
print("List of Search path of Module ",sys.path)
