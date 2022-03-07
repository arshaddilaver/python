" construct following pattern using nexted for loop"
size=int (input("enter size "))
for i in range(size*2):
    if i<=size:
        for j in range(i):
            print("*",end=" ")
        print("\n")
    else:
        for j in range(size*2-i):
            print("*",end=" ")
        print("\n")
