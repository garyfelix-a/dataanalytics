def checkage(age):
    if age < 18:
        raise ValueError("Age must be 18")
    else:
        print("You're eligible")
        
age = int(input("Enter your age: "))

try:
    checkage(age)
except ValueError as e:
    print(e)