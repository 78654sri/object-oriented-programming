#without existing one type of obj if there is no chance of existing another type of obj
class University:#outer class
    def __init__(self, name, location):
        self.name = name
        self.location = location
    class Department:#inner class
        def __init__(self, name, university):
            self.name = name
            self.university = university
        def m1(self):
            print("Department name is:", self.name)
uni=University()
de=uni.Department()
de.m1()
