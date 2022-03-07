"""Create Rectangle class with attributes length and breadth and methods to find area and
perimeter. Compare two Rectangle objects by their area.
"""

class Rectangle:
    length=0
    breadth=0  
    def __init__(self):
        self.length=float(input("Enter length"))
        self.breadth=float(input("Enter breadth"))

    def area1(self):
        area=self.length*self.breadth  
        return area

    def perimeter1(self):
        perimeter=2*(self.length+self.breadth)
        return perimeter


ch=int(input("enter choice 1 find area and perimtere of rectangle \n \
                           2 compare area of two rectangle "))

if ch==1:
    rect1=Rectangle()
    print("Area of Rectangle is {}".format(rect1.area1()))
    print("Perimeter of Rectangle is {}".format(rect1.perimeter1()))
elif ch==2:
    print("1st Rectangle ")
    rect1=Rectangle()
    rect1_area=rect1.area1()
    print("2nd Rectangle")
    rect2=Rectangle()
    rect2_area=rect2.area1()
    if (rect1_area<rect2_area):
        print("2nd Rectangle have larger area and area is {}".format(rect2_area))
    else:
        print("1st Rectangle have larger area and area is {}".format(rect1_area))
    if(rect1_area==rect2_area):
        print("Both having same area")

