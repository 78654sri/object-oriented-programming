class Test:
    a=9
    def __init__(self):
        Test.b=20
        Test.a=12
        print(self.a)
        print(Test.a)
    def m1(self):
        Test.c=0
        print(self.b)
        print(Test.a)
    
    @classmethod
    def m2(cls):
        cls.d=78
        cls.a=233
        Test.r=88
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        Test.s=99
        Test.a=34
        print(Test.a)
t=Test()
t.m1()
t.m2()
t.m3()
print(Test.a)
Test.h=0
print(Test.__dict__)
