x = 5
print(x > 3 and x < 10)

x = 10
print(x > 3 or x < 14)

x = 5
print(not(x > 14 and x < -1))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
y = x
x = y
print(x is z)
print(x is y)
print(x == y)
print(not(x != z))
print(x >= z)
