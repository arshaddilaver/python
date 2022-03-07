"6. Store a list of first names. Count the occurrences of ‘a’ within the list"

limit=int(input("enter limit"))

print("enter your first name")
first_name_lst=[]
for lim in range(limit):
    first_name=input()
    first_name_lst.append(first_name)

occur_A=sum([name.count('a')for name in first_name_lst])

print("occurrences of ‘a’ in the list is",occur_A)