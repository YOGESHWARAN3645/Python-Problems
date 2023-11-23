#If the ages of Ram, Shyam and Ajay are input through the keyboard.
#write a program to determine the youngest of the three.

ramAge=int(input("Ram Age ; "))
shyamAge=int(input("shyam Age ; "))
ajaiAge=int(input("Ajai Age ; "))


if(ramAge<shyamAge and ramAge<ajaiAge):
    print("Ram is youngest")
elif(shyamAge<ramAge and shyamAge<ajaiAge):
    print("Shyam is Youngest")
elif(ajaiAge<ramAge and ajaiAge<shyamAge):
    print("Ajai is Youngest")

           
