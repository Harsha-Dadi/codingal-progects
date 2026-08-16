print("Welcome to holiday planner")
print("Step 1: choose your destination")
print("Enter 1 for Beach holiday or Enter 2 for mountain holiday")
choice=int(input("Enter 1 or 2"))
if choice == 1:
    print("You have chosen Beach holiday")
    print("Step 2:Pick your beach holiday")
    print("Enter 1 or Swimming or Enter 2 for Sandcastle building")
    beach_activity=int(input("Enter 1 or 2"))
    if beach_activity == 1:
        print("You chosen :  swimming")
        print("Best time  :  morning ")
        print("Remember   :  Carry sunscreen and water")
    else:
        print("You chosen :  sand castle building")
        print("Best time  :  Evening ")
        print("Remember   :  Carry bucket and spade")
elif choice == 2:
    print("You have chosen mountain holiday")
    print("Step 2:Pick your mountain holiday")
    print("Enter 1 or hiking or Enter 2 for Camping")
    mountain_activity=int(input("Enter 1 or 2"))
    if mountain_activity == 1:
        print("You chosen :  Hiking")
        print("Best for  :  exploring trails")
        print("Remember   :  wear comfortable shoes")
    else:
        print("You chosen :  Camping")
        print("Best for  :  Seeing nature ")
        print("Remember   : Carry tent and flashlight")
else:
    print("Invalid choice Enter 1 for beach holiday and 2 for mountain holiday")

print("Your trip is ready enjoy your trip")
