#Rahul
#21mca035

from graphics import circle
from graphics.rectangle import *
from graphics.td_graphics import cuboid , sphere

r=int(input("Enter radius of circle"))
print("Area of Circle ",circle.area(r))
print("Perimeter of Circle ",circle.perimeter(r))
print("____________________________________________")
l=int(input("Enter length of rectangle "))
b=int(input("Enter breadth of rectangle "))
print("Area of Rectangle",area(l,b))
print("perimeter  of Rectangle",perimeter(l,b))
print("______________________________________________")
l=int(input("Enter length of cuboid "))
b=int(input("Enter breadth of cuboid "))
h=int(input("Enter length of cuboid "))
print("Area of cuboid",cuboid.area(l,b,h))
print("Perimeter of cuboid ", cuboid.perimeter(l,b,h))
print("__________________________________________________")
r=int(input("Enter radius of sphere"))
print("Area of sphere ",sphere.area(r))
print("surface area of Sphere ",sphere.perimeter(r))
print("_______________________________________________________")








