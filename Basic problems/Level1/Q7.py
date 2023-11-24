#If a five-digit number is input through the keyboard, 
#write a program to calculate the sum of its digits. 
#( Hint: Use the modulus operator '%')
d=0
sum=0
num=int(input("Number:"))
while d<5:
  sum= sum + int(num%10)
  num=num/10
  d=d+1
print("Sum;",sum)
