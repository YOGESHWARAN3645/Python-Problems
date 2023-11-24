#If the total selling price of 15 items and the total profit earned on them is input through the keyboard
#write a program to find the cost price of one item

totalPrice=float(input("Total Price:"))
totalProfit=float(input("Total Profit:"))
items=int(input("Items:"))
costPrice= totalPrice-totalProfit
single=costPrice//items
print("Cost Price:",costPrice,"Items:",items)
print("single:",single)
