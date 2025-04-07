# class Vehicle:
#     def __init__(self, name):
#         self.name = name
        
#     def start(self):
#         raise NotImplementedError("Subclasses must implement this method")
    
# class Car(Vehicle):
#     def start(self):
#         return "Engine Started"
    
# a = Vehicle("Four wheelers")


class Color: 
    def __init__(self):
        self.name = 'Green'
        self.lg = self.Lightgreen()
        
    def show(self):
        print('Name:', self.name)
    
    class Lightgreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'
            
        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)
            
outer = Color()
outer.show()

g = outer.lg
g.display()