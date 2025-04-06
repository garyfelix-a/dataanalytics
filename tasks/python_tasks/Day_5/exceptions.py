# for importing wrong module error
import wrong_module

li = [1,0,3,4,5] 
dic = {"name": "Rolex", "age": 35}
try:
    result1 = li[0] + li[1]
    result2 = li[1] + li[5]
    # for zero division error 
    print(result1)
    # for index out of range error
    print(result2)
    # for key error
    print(li["missing"])
    # for name error
    print(x)
    # for syntax error
    prin(result1)   
except ValueError as e:
    print("Invalid input:", e)
except ZeroDivisionError as e:
    print("Cannot divide by zero", e)
except IndexError as e:
    print("Index out of range:", e)
except KeyError as e:
    print("Key not found:", e)
except NameError as e:
    print("Name not found:", e)
except ImportError as e:
    print("Import fails:", e)
except SyntaxError as e:
    print("Code written incorrectly:", e)
# use this Exception when you're not sure what erros might occur. 
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("No error occurred")
finally:
    print("code executed")