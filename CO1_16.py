"""Create a single string separated with space from two strings by swapping the
character at position 1. """

string1=input("Enter String One")
string2=input("Enter String Two")

ch1_string1=string1[0]
ch2_string2=string2[0]

newstring=ch2_string2+string1[1:]+" "+ch1_string1+string2[1:]
print("New string is ",newstring)
