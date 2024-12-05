class Bird:
    wings=2
    @classmethod
    def fly(cls,name):
        print(f"{name} is flying with {cls.wings} wing")
B=Bird()
B.fly("parrot")
B.fly("eagel")

class Test:
    count=0
    def __init__(self):
        Test.count+=1
    
    @classmethod
    def getObjCount(cls):
        return cls.count
    
Test.getObjCount()
t1= Test()
t2= Test()
t3= Test()
t4= Test()
print(Test.getObjCount())