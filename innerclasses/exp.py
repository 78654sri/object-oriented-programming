class Employee:
    def __info__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Employee Number:",self.eno)
        print("Employee Name:",self.ename)
        print("Employee salary :",self.esal)
class Manager:
    @staticmethod
    def updateempsal(emp):
        emp.sal=emp.sal+1000
        emp.display()
emp=Employee(101,"basava",2344)
Manager.updateempsal(emp)#one class access the members of another class