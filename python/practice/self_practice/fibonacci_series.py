# n = 12

# a = 0
# b = 1

# for _ in range(n):
#     print(a, end=" ")
#     a,b = b, a+b

n = 5

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a+b
    count += 1