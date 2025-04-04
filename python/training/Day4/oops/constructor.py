class Car:
    brand = "Maruti"
    
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
car1 = Car("Dzire", 2025)
print(car1.brand)
print(car1.name, car1.year)

        