str = "racecar"
str2 = ""
n = len(str)
while n > 0:
    n = n - 1
    str2 += str[n]

print("Before Reverse:",str, "\nAfter Reverse:", str2)   

if str2 == str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
