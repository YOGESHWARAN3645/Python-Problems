#The distance between two cities (in km.) is input through the keyboard.
#Write a program to convert and print this distance in meters, feet, inches and centimeters.
km=int(input("Enter the Kilometer between two cities:"))
meters=km*1000
centimeter=km*100000
feet= km*3280.84
inches=km*39370.08

print("Meters:",meters)
print("Centimeter:",centimeter)
print("Feet:",feet)
print("Inches:",inches)
