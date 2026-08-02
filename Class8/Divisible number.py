numerator=int(input("Enter your numerator here: "))
denominator=int(input("Enter your denominator here: "))

if numerator%denominator == 0:
    print(f"{numerator} is divisible by {denominator}")
else:
    print(f"{numerator}is not divisible by {denominator}")