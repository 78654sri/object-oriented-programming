class Test:
    def __init__(self):
        self.a=10
        self.v=90
    def m1(self):
        self.c=45
        self.d=90
        del self.d
T=Test()
del T.v
T.m1()
T.e=99

print(T.a)
t1=Test()
print(T.__dict__) 
print(t1.__dict__)

#with in the class
# del self.variable

#outside the class
# del objref.variable
