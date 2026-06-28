temp=int(input("Enter temperature:"))
if temp > 56 or temp < -10:
    print("Invalid temperature! Please enter a value between -10°C and 56°C.")
else:
    if temp >=21<=38:
        print("Suitible to use light and soft clothes")
    else:
        print("Wear Jacket and pullover")
