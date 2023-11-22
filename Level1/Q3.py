#If the marks obtained by a student in five different subjects are input through the keyboard, 
#find out the aggregate marks and percentage marks obtained by the student. 
#Assume that the maximum marks that can be obtained by a student in each subject is 100.

print("Enter the Marks:")
tamil=int(input("Tamil:"))
english=int(input("English:"))
maths=int(input("Maths:"))
science=int(input("Science:"))
computer=int(input("Computer:"))

aggregate=tamil+english+maths+science+computer
percentage= aggregate/5.0 
print("Aggrerate:",aggregate)
print("Percentage:",percentage)
