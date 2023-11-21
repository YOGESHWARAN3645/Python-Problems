#Two numbers are input through the keyboard into two locations C and D. 
#Write a program to interchange the contents of C and D.
c=int(input("c:"))
d=int(input("d:"))

c=c+d
d=c-d
c=c-d 
print("c:",c)
print("d:",d)
