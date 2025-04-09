n = 43
flag = 1
i = 2
while i<n:
    if n%i == 0:
        flag = 0
        break
    i = i+1
if flag:
    print("prime")
else:
    print("not prime")