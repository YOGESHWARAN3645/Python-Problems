 #A five-digit number is entered through the keyboard. 
#Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.
num=int(input("num;"))
c=0
sums=num
copy=num
while True:
    num=int(num/10)
    c=c+1
    if(num==0):
        break;
print(c)
i=0
sum1=0
while i<c:
    sum1=sum1+(sums%10)*(10**(c-1)) 
    sums=int(sums/10) 
    c=c-1
print(sum1)

if(copy==sum1):
  print("equal")
else:
  print("not equal")
