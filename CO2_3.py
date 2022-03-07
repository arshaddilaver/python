"Find the sum of all items in a list"
n=int(input("enter range of list"))

lst1=[]
for i in range(n):
    lst1.append(int(input()))

print("sum of list is",sum(lst1))