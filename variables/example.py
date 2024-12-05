class Student:
    school_name="hjkwd" #static variable

    def __init_(self,name,rollno):
        self.name=name  #instance var
        self.rollno=rollno #instance var


    def info(self):
        x=10 #local var
        for i in range(x):
            print(i)