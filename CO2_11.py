"write lambda function to find area of square,rectangle and triangle"
ch=int(input("1   find area of square\n\
              2   find are of rectangle \n\
              3   find area of triangle \n"))

if ch==1:
  x=int(input("enter the length of one side of a square"))
  square=lambda x:x*x
  print("Area of square is ",square(x))
if ch==2:
  x=int(input("enter the length of rectangle"))
  y=int(input("enter the breadth of rectangel"))
  rectangle=lambda x,y:x*y
  print("Area of rectanble is ",rectangle(x,y))
if ch==3:
  x=int(input("enter the height of triangle"))
  y=int(input("enter the breadth of triangle"))
  triangle=lambda x,y:0.5*x*y
  print("Area of trinagle is ", triangle(x,y))
