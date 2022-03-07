"Print out all colors from color-list1 not contained in color-list2. "

colorlst1=[]
colorlst2=[]

range1=input("enetr size of list one")
print("enter color list 1")
for i in range(int(range1)):
    colorlst1.append(input())

range2=input("enter size of list two")
print("enter color list 2")
for i in range(int(range2)):
    colorlst2.append(input())

print(" all colors from color-list1 not contained in color-list2",set(colorlst1)-set(colorlst2))

