#A company insures its drivers in the following cases:
#If the driver is married.
#If the driver is unmarried, male & above 30 years of age.
#If the driver is unmarried, female & above 25 years of age.


class Driver():
    def __init__(self):
        self.gender=""
        self.marital=""
        self.age=0
    def insurance(self):
        if(self.marital=="M"):
             print("Insurance Available")
        elif(self.gender=="M" and self.marital=="U" and self.age>30):
            print("Insurance Available")
        elif(self.gender=="F" and self.marital=="U" and self.age>25):
            print("Insurance Available")
        else:
            print("Insurance Not Available")
            
d1=Driver()
d2=Driver()
d1.gender=input("Gender: ")
d1.marital=input("Marital: ")
d1.age=int(input("Age: "))
d1.insurance()
       
            

