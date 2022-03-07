"""8. Get a string from an input string where all occurrences of first character replaced with
‘$’, except first character.
[eg: onion -> oni$n]"""

string1=input("Enter a word")
fstchr=string1[0]
new_str=fstchr+string1[1:].replace(fstchr,'$')
print("{}->{}".format(string1,new_str))

