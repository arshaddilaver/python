"Find gcd of 2 numbers. "

number1=int(input("Enter first number"))

number2=int(input("Enter second number"))

factors_number1= [i for i in range(1,number1+1) if number1%i==0]
factors_number2= [i for i in range(1,number2+1) if number2%i==0]

common_factors=set(factors_number1)&set(factors_number2)
if len(common_factors)!=0:
    gcd=max(common_factors)
    print("Greatest Common Divisor is ",gcd)
    