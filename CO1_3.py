"""
List comprehensions:
(a) Generate positive list of numbers from a given list of integers
(b) Square of N numbers
(c) Form a list of vowels selected from a given word
(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)

"""
"(a)"
#genearte list of integers

limit=int(input("enter Limit"))
integer_lst=[]
for i in range(limit):
    num=int(input())
    integer_lst.append(num)
#select  +ve numbers from list
positive_list=[num for num in integer_lst if num>0 ]
print("postive integers list is ",positive_list)

"(b) Square of N numbers"

limit=int(input("enter limit"))
nnumber_list=[]

for i in range(limit+1):
    nnumber_list.append(i)

sq_num_list=[num*num for num in nnumber_list]
print("square number list",sq_num_list)

'(c)Form a list of vowels selected from a given word'

vowels="aAEeIiOoUu"
word=input("enter a word")
vowelpresentword= [let for let in word if let in vowels]
print("vowels in word",vowelpresentword)

"(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)"

word=input("enter a word")
ordinal_values=[ord(let)for let in word]
print("ordinal values of given word",ordinal_values)