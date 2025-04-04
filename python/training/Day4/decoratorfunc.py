def decorator(func):
    def wrapper():
        print("Before calling function")
        func()
        print("After calling function")
    return wrapper

@decorator
def greet():
    print("Hello, welcome!")
    
greet()