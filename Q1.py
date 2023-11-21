#1. Ramesh's basic salary is input through the keyboard. 
#His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. 
#Write a program to calculate his gross salary.

basicSalary=int(input("Basic Salary:"))
da=(40/100)*basicSalary
ra=(20/100)*basicSalary
grossSalary=basicSalary+da+ra