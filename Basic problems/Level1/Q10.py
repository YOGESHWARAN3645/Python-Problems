#In a town, the percentage of men is 52. 
#The percentage of total literacy is 48. 
#If total percentage of literate men is 35 of the total population
#write a program to find the total number of illiterate men and women if the population of the town is 80,000.
totalPopulation= 80000
men= int((52/100)*totalPopulation)
women= totalPopulation-men
totalLiteracy=(35/100)*totalPopulation
menLiteracy=int((35/100)*men)
womenLiteracy= totalLiteracy-menLiteracy
print("Men:",men)
print("Women:",women)
print("men Literacy:",menLiteracy)
print("Women Literacy:",womenLiteracy)
print("Total Literacy:",totalLiteracy)
