a=10
b=20
c=30

average=(a+b+c)/3
print("the average is ",average)
if average > a and average > b and average > c :
    print("%d is greater than %d,%d and %d" %(average,a,b,c))
elif average > a and average > b :
    print("%d is greater than %d,%d" %(average,a,b))
elif average > a and average > c :
    print("%d is greater than %d,%d" %(average,a,c))
elif average > b and average > c :
    print("%d is greater than %d,%d" %(average,b,c))
elif average > a:
    print("%d is greater than %d" %(average,a))
elif average > b:
    print("%d is greater than %d" %(average,b))
elif average > c:
    print("%d is greater than %d" %(average,c))
else:
    print("Invalid input")