print("Haf pyramid pattern of triangle")
n=int(input("How many rows for your pattern?"))

for i in range(n):
    for j in range(i+1): 
        print("*",end="")
    print()