class p:
    def m1(self):
        print("parent class method")
class C(P):
    def m2(self):
        print("child class method")

c=C()
c.m1()
c.m2()