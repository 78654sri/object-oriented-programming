class Student:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
n=int(input("enter no of students:"))
students=[]
for i in range(n):
    student = Student()
    name = input("enter name")
    student.setName(name)
    age = int(input("enter age"))
    student.setAge(age)
    students.append(student)
for s in students:
    print(student.getName())
    print(student.getAge())

    