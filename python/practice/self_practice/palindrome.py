n = 121
temp = n
rev = 0

while n>0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10    # floor division
    
print("palindrome" if temp == rev else "not palindrome")