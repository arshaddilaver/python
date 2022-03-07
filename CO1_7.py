"""7. Enter 2 lists of integers. Check (a) Whether list are of same length 
(b) whether list sums to same value (c) whether any value occur in both"""

lst1=[10,30,50,30,600,70]
lst2=[9,7,50,78,60,440,700]

"Check (a) Whether list are of same length "

if lst1==lst2:
    print("List Have same lentgh")
else:
    print("list is not in same length")

if sum(lst1)==sum(lst2):
    print("two list have same sum")
else:
    print("sum is not same")

set_lst1=set(lst1)
set_lst2=set(lst2)

"& used to perform union opertion in sets" 
print("{} elements are common in two lists".format(set_lst1&set_lst2))