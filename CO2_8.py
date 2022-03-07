"Accept a list of words and return length of longest word "
word_list=[]
limit=int(input("enter size of list"))
print('enter words')
for i in range(limit):
  word_list.append(input())
print(max(len(i) for i in word_list)):
