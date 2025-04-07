from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car started")
        
    def stop(self):
        print("Car stops when brake is pressed")

car = Car()
car.start()
car.stop()