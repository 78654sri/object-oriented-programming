class Person:
    def __init__(self, name, dd,mm,yy):
        self.name = name
        self.dob=self.Dob(dd,mm,yy)
    def info(self):
        print(f"Name: {self.name}")
        self.dob.display()
    class Dob:
        def __init__(self,dd,mm,yy):
            self.dd = dd
            self.mm=mm
            self.yy=yy
        def display(self):
            print(f"Date of Birth: {self.dd}/{self.mm}/{self.yy}")
p=Person("bd",3,4,5432)