"generate all factors of a number"
number=int(input('enter a number'))
factors=[i for i in range(1,number+1) if number%i==0]
print("factors of {} are {}".format(number,factors))
