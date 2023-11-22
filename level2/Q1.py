#While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10. 
#If quantity and price per item are input through the keyboard, 
#write a program to calculate the total expenses.
quantity= int(input("Qty:",))
price = float(input("price:"))
totalExpenses= quantity*price
if(totalExpenses>10):
  discount= (10/100)*totalExpenses
  totalExpenses=totalExpenses-discount
  print("Total Expenses : ",totalExpenses)
else:
  print("Total Expenses : ",totalExpenses)
  
