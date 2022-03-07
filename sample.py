
from re import A


class Demo:
    
    def __init__(self):
        self.z=int(input("enter number"))


    def __add__(self,b):
        print("first b valube",self.z)
        print("second b value ",b.z)

        c=self.z*b.z

        return c
    
b1=Demo()
c1=Demo()
#print(a1+b1)
print(b1+c1)






