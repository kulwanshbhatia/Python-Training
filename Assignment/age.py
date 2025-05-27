age=int(input('Enter your age : '))
if age <0:
    print("Enter Valid age")
elif age <18:
    print("Not allowed to vote")
elif  age >=18 and age<79  :
    print("Allowed to vote")
else:
    print("Senior Citizen")