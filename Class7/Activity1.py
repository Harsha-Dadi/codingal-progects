var=3

if type(var) is int:
    print("True")
else:
    print("False")

var1=3.0

if type(var1) is not float:
    print("True")
else:
    print("False")

x=10
y=10

if x is y:
    print("they are the same identity")

y=11

if x is not y:
    print("they have the different identities")