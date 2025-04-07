class NotEligible(Exception):
    pass

def checkage(age):
    if age < 18:
        raise NotEligible("Age must be 18")
    else:
        print("You are eligible to vote")
        
age = int(input("Enter your age: "))        

try:
    checkage(age)
except NotEligible as e:
    print("Error: ", e)