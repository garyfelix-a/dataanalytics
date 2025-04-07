class Parent:
    def show(self):
        print("Inside Parent")
        
class Child(Parent):
    def show(self):
        super().show()
        print("Inside Child")
        
obj = Child()
obj.show()
