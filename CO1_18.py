"Merge two dictionaries. "
size=int(input("enter size"))
dict1={}
print("Key must be uniques")
for i in range(size):
    k=input("enter key")
    dict1[k]=input("enter value")


size=int(input("enter size"))
dict2={}
print("Key must be uniques")
for i in range(size):
    k=input("enter key")
    dict2[k]=input("enter value")

dict1.update(dict2)

print("Merged dict is  :",dict1)

