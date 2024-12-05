# when we are inheriting the abstract class we always have to provide the implementation for the abstract methods
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    def apply_horn(self):
        print("Beep Beep!")
class Car(Vehicle):
    def start(self):
        print("Car has started")
    
    def stop(self):
        print("Catr has stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike has started")
    
    def stop(self):
        print("Bike has stopped")

    
car =Car()
car.apply_horn()
car.start()
car.stop()