#if we are using instance varibles in a method i.e instance method
class Student:
    school_name="vercel"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getStudentInfo(self):#instance method
        print(f"Name: {self.name} Age: {self.age}")

    @classmethod
    def getSchoolName(cls):
        print('school Name:',cls.school_name)

    @staticmethod
    def getSum(a,b):
        sum=a+b
        return sum