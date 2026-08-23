value=int(input("Enter your number:"))
power=int(input("Enter the power:"))
result=1
for i in range(power):
    result=result*value

print(f" {power} power of {value} is {result}")