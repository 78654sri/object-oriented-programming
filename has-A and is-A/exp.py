# we can use members of one class inside another class by using:
# composition(Has-A) and inheritance(IS-A)

class Engine:
    def __init__(self):
        self.power="123kw"
    def useEngine(self):
        print("Engine is used")
class Car:
    def __init__(self):
        self.engine = Engine()
    def useCar(self):
        print("car required engine functionalities")
        self.engine.useEngine()
        print(self.engin.power)
c=Car()
c.useCar()