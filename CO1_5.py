"(5)Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead."

limit=int(input("enter limit"))
out_list=[]
for i in range(limit):
    number=int(input())
    if number<100:
        out_list.append(number)
    else:
        out_list.append('over')

print(out_list)

