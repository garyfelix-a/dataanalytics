# try:
#     x=10/0
# except ZeroDivisionError:
#     print("Divide By Zero Exception")
# finally: 
#     print("Completed execution")    


try:
    num = int(input("Enter a number:"))
    result = 10/num
# if we give exception on top of all exceptions(ArithmeticError likewise), it won't work, because exception itself will handle all the exceptions 
except Exception as e: 
    print("An unexpected error occurred:", e)
except ValueError as e:
    print("Invalid input:", e)
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
else:
    print(f"Result :{result}")
finally:
    print("Completed execution")