cp=int(input("Enter cost price:"))
sp=int(input("Enter sales price:"))

if sp>cp:
    print("It is a Profit of ",sp-cp)
else:
    print("It is a Loss")