#If a five-digit number is input through the keyboard, 
#write a program to print a new number by adding one to each of its digits. 
#For example, if the number that is input is 12391 then the output should be displayed as 23402.

num=int(input("Number:"))
s=num
c=0
while True:
  num=num/10
  c=c+1
  if(num<10):
    break:
#while c>0:
  num=s//(10**c-1)
  print(num)
  
  
