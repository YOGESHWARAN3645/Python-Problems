 #The length & breadth of a rectangle and radius of a circle are input through the keyboard. 
 #Write a program to calculate the area & perimeter of the rectangle, and the area & circumference of the circle.
length=float(input("Length:"))
breadth=float(input("Breadth:"))
radius=float(input("Radius:"))
areaOfRectangle= length*breadth
perimeterOfRectangle=2*(length+breadth)
areaOfCircumference=2*(22/7)*radius

print("Area of Rectangle:",areaOfRectangle)
print("Perimeter of Rectangle:",perimeterOfRectangle)
print("Area of Circumference:",areaOfCircumference)
