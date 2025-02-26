class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length*self.breadth)
    
class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height=h
        super().__init__(l,b)

    def volume(self):
        return self.length*self.breadth*self.height
c=Cuboid(2,4,2)
print(c.volume())