num = int(input("Enter a number for Fibonacci series: "))

# 0 1 1 2 3 5 8 13

n1 = 0
n2 = 1
n3 = 0
print(n1)
print(n2)

while n3 < num:
    n3 = n1 + n2
    print(n3)
    n1, n2 = n2, n3
    