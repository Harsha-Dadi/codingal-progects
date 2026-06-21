amount=int(input("Enter the amount:"))

Pound100=amount//100
Pound50=(amount%100)//50
Pound10=(amount%50)//10

print("There are ",Pound100,"100 pound bills")
print("There are ",Pound50,"50 pound bills")
print("There are ",Pound10,"10 pound bills")