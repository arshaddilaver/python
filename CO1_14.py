"Accept an integer n and compute n+nn+nnn. "


number=input("Enter number")
rep=int(input("repeatiton"))
sum=0
for i in range(1,rep+1):
    sum=sum+int(number*i)
print(sum)