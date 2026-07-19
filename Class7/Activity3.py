sub1=int(input("Enter subject grade:"))
sub2=int(input("Enter subject grade:"))
sub3=int(input("Enter subject grade:"))
sub4=int(input("Enter subject grade:"))
sub5=int(input("Enter subject grade:"))

avg= (sub1+sub2+sub3+sub4+sub5)//5
validrange=range(0,101)

if avg not in validrange:
    print("Invalid")
elif avg in range(75,101):
    print("Good performance")
elif avg in range(40,75):
    print("average performance")
elif avg in range(0,40):
    print("Poor performance")