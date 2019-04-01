def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(9)

print(mydoubler(11))
