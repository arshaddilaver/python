"Find biggest of 3 numbers entered. "

num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

if num1>num2:
    if num1<num3:
        print("Biggest number is {}".format(num3))
    else:
        print("Biggest number is {}".format(num2))
else:
    if num2>num3:
        print("Bigget number is {}".format(num2))
    else:
        print("Biggest number is {}".format(num3))