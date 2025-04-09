from functools import reduce

x = [1,2,3,4,5]
f = reduce(lambda a,b: a+b, x)
print(f)