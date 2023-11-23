#The marks obtained by a student in 5 different subjects are input through the keyboard. 
#The student gets a division as per the following rules: 
#Write a program to calculate the division obtained by the student.
'''Percentage above or equal to 60 - First division
   Percentage between 50 and 59 - Second division
   Percentage between 40 and 49 - Third division
   Percentage less than 40 – Fail'''

tamil=int(input("Tamil:"))
english=int(input("English:"))
maths=int(input("Maths:"))
science=int(input("Science:"))
cs=int(input("cs:"))

percentage= (tamil+english+maths+science+cs)/5

if(percentage>=60):
   print("First division")
elif(percentage>=50 and percentage <=59):
   print("Second division")
elif(percentage>=40 and percentage <=49):
   print("Third division")
elif((percentage<40):
   print("Fail")


