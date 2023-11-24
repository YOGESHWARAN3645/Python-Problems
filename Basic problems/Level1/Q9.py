#If a four-digit number is input through the keyboard, 
#write a program to obtain the sum of the first and last digit of this number.

num=int(input("Number:"))
c=0
sums=num
while True:
    num=int(num/10)
    c=c+1
    if(num==0):
        break;
num= int(sums%10)
num=int(num+(sums/(10**(c-1))))
print(num)
