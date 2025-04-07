# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# operation = input("Enter which operation to perform (+, -, *, /, %): ")
# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     if num2 == 0:
#         return "Division By Zero is Not Allowed"
#     return num1 / num2

# def mod(num1, num2):
#     if num2 == 0:
#         return "Modulo by zero is not allowed"
#     return num1 % num2

# if operation == "+":
#     print(add(num1, num2))
# elif operation == "-":
#     print(sub(num1, num2))
# elif operation == "*":
#     print(mul(num1, num2))
# elif operation == "/":
#     print(div(num1, num2))
# elif operation == "%":
#     print(mod(num1, num2))


# Type 2

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
op = input("Enter the symbol(+, -, *, /, %)")

calc = lambda x, y, z: x + y if z == "+" else x - y if z == "-" else x * y if z == "*" else x / y if z == "/" else x % y
print(calc(num1, num2, op))