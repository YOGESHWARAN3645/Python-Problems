#A cashier has currency notes of denominations 10, 50 and 100.
#If the amount to be withdrawn is input through the keyboard in hundreds
#find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
withdraw= int(input("Withdraw Amount :"))
ten=10
fifty=50
hundred=100

hundred= withdraw//100
withdraw=withdraw%100
fifty= fifty//50
withdraw= withdraw%50
ten=withdraw//10
balance=withdraw%10
print("Hundreds:",hundred)
print("Fifty:",fifty)
print("Ten:",ten)
print("Balance:",balance)

