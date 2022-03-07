
"Count the number of characters (characters frequency) in a string" 
string=input("enter a string")
ch_count={str:string.count(str)for str in set(string)}
print(ch_count)
