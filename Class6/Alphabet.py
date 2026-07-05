alphabet=(input("Enter value to see if alphabet:"))

if len(alphabet)!=1:
    print("Please enter single character")
elif (alphabet>='a'and alphabet<='z')or(alphabet>='A'and alphabet<='Z'):
    print("it is in the alphabet")
else:
    print("the given value isn't in the alphabet")