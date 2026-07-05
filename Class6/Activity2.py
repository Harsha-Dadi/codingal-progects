a=2
b=3
c=3

print(not(a==b))
print(not(c==b))

a="Hi"
b="Hello"

if not(a==b):
    print(a,"and",b,"are different")

a=4
b=5

if not((a==1)==(b==5)):
    print("Hello")

a=int(input("Enter a number"))

if not(a%2==0):
    print(a,"is odd")