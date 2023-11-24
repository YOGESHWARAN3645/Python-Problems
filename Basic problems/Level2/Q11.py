#Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard.
#A triangle is valid if the sum of all the three angles is equal to 180 degrees.
angle1=int(input("Angle1: "))
angle2=int(input("Angle2: "))
angle3=int(input("Angle3: "))

total= angle1+angle2+angle3
if(total==180):
  print("equal")
else:
  print("Not equal")
