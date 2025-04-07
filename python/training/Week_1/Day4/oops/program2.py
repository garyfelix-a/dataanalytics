class Car:
    # class variable
    brand = "Maruti"
    
    def __init__(self, name, year):
        # instance variables
        self.name = name
        self.year = year
        
# creating objects
car1 = Car("Dzire", 2025)

# access class and instance variables
print(car1.brand)   # class variable
print(car1.name, car1.year)  # instance variable

# modify instance variables
car1.name = "Ciaz"
print(car1.name)  # updated instance variable

# modify class variables

car1.brand = "Mahindra"
print(car1.brand) # updated class variable

        