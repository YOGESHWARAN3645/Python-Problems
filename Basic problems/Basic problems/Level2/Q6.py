#Write a program to calculate the salary as per the following table:
employee=input("gender:")
experience=int(input("Experience:"))
qualification=input("Degree:")
if(employee=='male'):
  if(experience>= 10 and qualification=="pg"):
    print("salary= 15000")
  elif(experience>= 10 and qualification=="ug"):
    print("salary= 10000")
  elif(experience< 10 and qualification=="pg"):
    print("salary= 10000")
  elif(experience< 10 and qualification=="ug"):
    print("salary= 7000")
elif(employee=="female"):
  if(experience>= 10 and qualification=="pg"):
    print("salary= 12000")
  elif(experience>= 10 and qualification=="ug"):
    print("salary= 9000")
  elif(experience< 10 and qualification=="pg"):
    print("salary= 10000")
  elif(experience< 10 and qualification=="ug"):
    print("salary= 6000")
