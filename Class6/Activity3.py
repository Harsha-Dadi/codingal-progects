weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(m):"))

bmi=weight/height**2
if bmi<=18.4:
    print("you are under weight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are over weight")
elif bmi<=39.9:
    print("you are obese")
else:
    print("you are severly obese")