"4. Count the occurrences of each word in a line of text."

line_of_text=input("enter line of text")
#split line of text into words
word_lst=line_of_text.split(' ')
#remove repeated words from the list by convert list into set (sets not allow repeated values)
word_set=set(word_lst)
occurence_dict={} #For store occurrence of words in the line of text
for word in word_set:
    occurence_dict[word]=word_lst.count(word)
print("Occurence :",occurence_dict)