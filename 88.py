# To find a number divisible by another number or not
n = int(input("Enter a number :"))
x = int(input("Enter another number :"))
if n % x == 0:
    print(x, "is divisible by", n)
else:
    print(x, "is not divisible by ", n)
