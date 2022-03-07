"""

Python program to copy odd lines of one file to other

"""

with open("sample.txt",'r') as file:
    output=file.readlines()

print("\n Content of first file is          :",output)

with open("sample1.txt",'w') as file:
    file.write(str(output[::2])[1:-1])
print("\n Content of second file is          :",str(output[::2])[1:-1])