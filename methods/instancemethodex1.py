#instance methods
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Name: {self.name}")
        print(f"marks: {self.marks}")
    def grade(self):
        if self.marks>=80:
            return "A"
        elif self.marks>=60:
            return "B"
        else:
            return "C"
#creating an object
n=int(input('Enter number of students:')) 
for i in range(n):
    name=input('Enter name of student:')
    marks=int(input('Enter marks of student:'))
    s=Student(name,marks)
    s.display()
    print(f"Grade: {s.grade()}")
    print()