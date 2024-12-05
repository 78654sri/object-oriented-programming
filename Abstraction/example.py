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
# we cannot create objects of an abstract class as they are only ment to be inherited