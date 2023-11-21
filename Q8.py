#If a five-digit number is input through the keyboard,
#write a program to reverse the number.


num=int(input("num;"))
c=0
sums=num
while True:
    num=int(num/10)
    c=c+1
    if(num==0):
        break;
print(c)
i=0
sum=0
while i<c:
    sum=sum+(sums%10)*(10**(c-1)) 
    sums=int(sums/10) 
    c=c-1
print(sum)
