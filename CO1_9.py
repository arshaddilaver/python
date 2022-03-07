"""9. Create a string from given string where first and last characters exchanged. [eg: python -
> nythop]"""

string=input("enter a string")

first_ch=string[0]
last_ch=string[-1]
newstr=last_ch+string[1:-1]+first_ch
print("{}->{}".format(string,newstr))