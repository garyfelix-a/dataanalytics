a = [1, 2, 3, 2, 1, 4]
b = []

# method 1
# for i in a:
#     if i not in b:
#         b.append(i)
        
# print(b)

# method 2
b = set(a)
print(list(b))
