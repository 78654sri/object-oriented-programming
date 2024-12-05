class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getInfo(self):
        print('car Name:{},Model: {},color: {}'.format(self.name,self.model,self.color))
class Employee:
    def __init__(self, name, no,car):
        self.name = name
        self.no = no
        self.car=car
    def info(self):
        return f"Name: {self.name}, Employee No: {self.no}, Car: {self.car.getinfo()}"
car =Car("innova","2.3v","grey")
emp = Employee("Rahul", 123, car)
emp.info()