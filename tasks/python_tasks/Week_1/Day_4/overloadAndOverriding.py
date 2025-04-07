# method overloading using default parameters
# class MathOperation:
#     def add(self, a, b=0, c=0):
#         return a + b + c

# obj = MathOperation()
# print(obj.add(5))
# print(obj.add(5, 2))
# print(obj.add(5, 2, 1))

# method overriding using *args
# class MathOperation:
#     def add(self, *args):
#         return sum(args)
    
# obj = MathOperation()
# print(obj.add(5))
# print(obj.add(5, 4))
# print(obj.add(5, 4, 4, 3))

# method overriding 
class Parent:
    def display(self):
        print("Parent")
        
class Child(Parent):
    def display(self):
        print("Child")
        
obj = Child()
obj.display()   # overridden method