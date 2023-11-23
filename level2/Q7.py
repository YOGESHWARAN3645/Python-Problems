#If cost price and selling price of an item is input through the keyboard, 
#write a program to determine whether the seller has made profit or incurred loss. 
#Also determine how much profit he made or loss he incurred.

costPrice=float(input("Cost price: "))
sellingPrice=float(input("Selling price: "))

profit= sellingPrice-costPrice
if(profit<0):
  print("Loss :",(profit/costPrice)*100)
elif(profit>0):
  print("Profit :",(profit/costPrice)*100)

  
