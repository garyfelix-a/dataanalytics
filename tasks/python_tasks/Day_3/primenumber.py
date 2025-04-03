n = int(input("Enter the number : "))

i=2
count = 1
while i<n:
    if n%i==0:
        count = 0
        break
    i+=1
   
if n < 2:
    print(n, " is neither prime nor composite") 
elif count:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")