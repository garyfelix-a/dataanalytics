# Defining and calling a function
def greeting():
    print("Hello, welcome!")
    
greeting()

# Function with parameters

def name(name):
    print("Helle", name)
    
name("Kevin Nash")

# Function with return values

def add(a, b):
    return a + b

print(add(1, 2))

# Default parameter value

def defValue(name="Brock"):
    print("Hey", name)
    
defValue()
defValue("Lesnar")

# Function with multiple return values
# type 1
def ageCheck(age):
    if age > 18:
        return "You're an adult"
    elif age < 18:
        return "You're a minor"
    else:
        return "You're exactly 18"

print(ageCheck(10))

# type 2

def get_values():
    name = "Ash"
    age = 39
    return name, age

n, a = get_values()
print("Name: ", n, "| Age: ", a)

# Function with multiple arguments

def add_all(*numbers):
    return sum(numbers)   # here sum is the predefined function

print(add_all(1,2,3,4,5))

# Function with **kwargs (keyword arguments)

def info(**details):
    for key, value in details.items():   # instead of giving keys(), we are using items()
        print(key, ":", value)
        
info(name="George", age=45, city="Chennai")