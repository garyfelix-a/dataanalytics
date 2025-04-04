# s1 = "Hey Buddy!!!"
# s2 = lambda func: func.upper()

# print(s2(s1))

# n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

# print(n(2))
# print(n(-1))
# print(n(0))

# Square of a num
# square = lambda x: print(x**2)
# square(2)

# list = [lambda arg=x: arg*10 for x in range(1, 5)]
# for i in list:
#     print(i())

# odd or even number
# oddOrEven = lambda num: "Odd" if num%2!=0 else "Even"
# print(oddOrEven(22))

# calculator using lambda function
# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))
# op = input("Enter the symbol(+, -, *, /, %)")

# calc = lambda x, y, z: x + y if z == "+" else x - y if z == "-" else x * y if z == "*" else x / y if z == "/" else x % y
# print(calc(num1, num2, op))

# filter option
# n = [1,2,3,4,5]
# even = filter(lambda x: x % 2 == 0, n)
# print(list(even))

# map option
# a = [1,2,3,4,5]
# b = map(lambda x: x * 2, a)
# print(list(b))

from functools import reduce

# reduce option
red = [1,2,3,4,5]
redFunc = reduce(lambda x, y: x * y, red)
print(redFunc)