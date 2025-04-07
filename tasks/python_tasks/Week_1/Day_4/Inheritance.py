# single inheritance
# class Vehicle:
#     def show(self):
#         print("Vehicle Class")
    
# class Car(Vehicle):
#     def display(self):
#         print("Car Class")
        
# obj = Car()
# obj.show()
# obj.display()

# Multiple Inheritance
# class Parent1:
#     def feature1(self):
#         print("Feature from Parent1")
        
# class Parent2: 
#     def feature2(self):
#         print("Feature from Parent2")

# class Child(Parent1, Parent2):
#     def feature3(self):
#         print("Feature from Child")
        
# obj = Child()
# obj.feature1()
# obj.feature2()
# obj.feature3()

# Multi Level Inheritance
# class GrandParent:
#     def display1(self):
#         print("Grand Parent")
        
# class Parent(GrandParent):
#     def display2(self):
#         print("Parent")
        
# class Child(Parent):
#     def display3(self):
#         print("Child")

# obj = Child()
# obj.display1()
# obj.display2()
# obj.display3()

# Hierarchical Inheritance
# class Parent:
#     def display1(self):
#         print("Parent")

# class Child1(Parent):
#     def display2(self):
#         print("Child 1")

# class Child2(Parent):
#     def display3(self):
#         print("Child 2")
        
# obj1 = Child1()
# obj2 = Child2()

# obj1.display1()
# obj1.display2()

# obj2.display1()
# obj2.display3()

# Hybrid Inheritance
# Class B and C extends Class A and Class D extends B and C.
# Multilevel + Multiple = Hybrid Inheritance
# class A:
#     def display1(self):
#         print("Class A")
        
# class B(A):
#     def display2(self):
#         print("Class B")

# class C(A):
#     def display3(self):
#         print("Class C")
        
# class D(B, C):
#     def display4(self):
#         print("Class D")
        
# obj = D()
# obj.display1()
# obj.display2()
# obj.display3()
# obj.display4()
                       
# class Parent(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def details(self):
#         print(self.name)
#         print(self.age)
    
# class Child(Parent):
#     def __init__(self, name, age, city):
#         super().__init__(name, age)
#         self.city = city
    
#     def details(self):
#         print("My Name is: {}".format(self.name))
#         print("My Age is: {}".format(self.age))
#         print("My City is: {}".format(self.city))
        

# obj = Child('Randy', 45, "New Orleans")
# obj.details()