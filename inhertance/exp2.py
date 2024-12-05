class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eatAndDRINK(self):
        print(f'{self.name} is eating and drinking')
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name)
        self.age=age
        self.salary=salary
    def work(self):
        print(f'{self.name} is working')
    def empInfo(self):
        print(f'Name: {self.name}, Age: {self.name}, Salary: {self.salary}')
e=Employee("durga",23,2332,32233)
e.empInfo()
e.work()
e.eatAndDRINK()