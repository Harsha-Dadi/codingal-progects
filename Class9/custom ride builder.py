print("WELCOME TO CUSTOM RIDE BUILDER!!!")

print("step 1 : choose your vehicle type")
var=int(input("Enter 1 for bike or enter 2 for car :"))
if var == 1:
    print("Your choice was a bike")
    print("Step 2: choose your bike type :")
    bike_type=int(input("Enter 1 for mountain bike or Enter 2 for scooty"))
    if bike_type == 1:
        print("Your choice was mountain bike")
        print("Mountain bike speed= 120kmp/hr")
        print("Suitable for dry conditions")
    elif bike_type == 2:
        print("Your choice was scooty")
        print("Mountain bike speed= 90kmp/hr")
        print("Suitable for city conditions")
    else:
        print("INVALID INPUT")
elif var == 2:
    print("Your choice was a car")
    print("Step 2: choose your car type :")
    car_type=int(input("Enter 1 for cidan or Enter 2 for SUV"))
    if car_type == 1:
        print("Your choice was Cidan")
        print("Cidan speed= 190kmp/hr")
        print("Suitable for city conditions")
    elif car_type == 2:
        print("Your choice was SUV")
        print("SUV speed= 150kmp/hr")
        print("Suitable for Mountain conditions")
    else:
        print("INVALID INPUT")

else:
    print("INVALID INPUT")

print("THANK YOU FOR TIME at CUSTOM RIDE BUILDER")