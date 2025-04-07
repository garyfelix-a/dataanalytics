class Car:
    brand = "Maruti"
    
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    def __str__ (self):
        return f"New {self.name} is launched in the year {self.year}"
        
car1 = Car("Dzire", 2025)
print(car1)

        