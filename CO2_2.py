"Generate Fibonacci series of N terms"

n_terms=int(input("Enter no.of terms"))
a=0
b=1
c=0
print(0)
print(1)

for i in range(0, n_terms-2):
    c = a + b
    a = b
    b = c
    print(b)
