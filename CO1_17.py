"Sort dictionary in ascending and descending order. "

size=int(input("enter size"))
dict={}
print("Key must be uniques")
for i in range(size):
    k=input("enter key")
    dict[k]=input("enter value")

print("Dictionary is ::  ",dict)
ascending_sorted_dict={}
descending_sorted_dict={}

for i in sorted(dict.keys()):
    ascending_sorted_dict[i]=dict[i]

for i in reversed(sorted(dict.keys())):
    descending_sorted_dict[i]=dict[i]


print("Sort dictionary in ascending order    :",ascending_sorted_dict)

print("Sort dictionary in descending order    :",descending_sorted_dict)


