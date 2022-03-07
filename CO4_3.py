"""
3. Create a class Rectangle with private attributes length and width. 
Overload ‘<’ operator
to compare the area of 2 rectangles.
"""
class Rectangle:
    __length=0
    __width=0
    area=0

    def __init__(self):
        self.__length=int(input("Enter length"))
        self.__width=int(input("Enter width"))
        self.area=self.__length*self.__width
    
    def __lt__(self,obj):
        print(self.area)
        print(obj.area)
        return self.area<obj.area

obj1=Rectangle()
obj2=Rectangle()
#print(obj1.__length)
print(obj1<obj2)
if(obj1<obj2):
    print("second rectangle have larger area ",obj2.area)
else:
    print("first rectangle have larger area ",obj1.area)
